import random
from flask import Flask, request, render_template, jsonify 
from flask_socketio import SocketIO, emit


import eventlet
eventlet.monkey_patch()

class Config:
    """Base config."""

    SECRET_KEY = "d75ebc83df8b212663637e33"  # environ.get('SECRET_KEY')
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    """ FLASK Production Configurations """
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False

    """ SocketIO Production Configurations """
    LOGGER = False
    ENGINEIO_LOGGER = False


""" Instanciates flask app (used for API calls) """
app = Flask(__name__)
app.config.from_object(Config)  # Using flask configurations

""" Instanciates socketio object (used for realtime communication) """
socketio = SocketIO(app, policy_server=False, manage_session=False, async_mode='eventlet', cors_allowed_origins="*")

""" A stucture that maps session ID to sid """
interactive_screens: dict[str, str] = {}


@app.route("/")
def index():
    """
    Endpoint used to access interactive board webpage.
    """
    return render_template("index.html")

@app.route("/log")
def log():
    return jsonify(
        greeting=["hello", "world"],
        date="Aujourd'hui",
        screens=list(interactive_screens.keys())
    )

@app.route("/doc")
def doc():
    """
    Endpoint used to access the API documentation.
    """
    return render_template("doc.md")


@app.route("/draw/<id>", defaults={"displayNum": None}, methods=["GET", "POST"])
@app.route("/draw/<id>/<displayNum>", methods=["GET", "POST"])
def draw(id, displayNum=None):
    """
    Endpoint used to draw a shape on the interactive board.
    """
    print(f"> ENDPOINT /draw")
    print(f"> CATCH")
    print(f"> ENDPOINT /draw")
    shape = request.json
    if id in interactive_screens.keys():
        print(f"> {id}")
        print(f"> {shape}")
        displayStr = f"/{displayNum}" if displayNum else ""
        socketio.emit(f"draw{displayStr}", shape, room=interactive_screens[id])
        print(f"draw on {id}{displayStr} {shape}")
    return "ok"


@socketio.on("connect")
def connection():
    """
    Connect a new interactive board.
    """
    id = str(random.randint(100000, 999999))
    interactive_screens[id] = request.sid
    emit("sessionID", id, to=request.sid)
    print(f"connect {request.sid} with id({id})")


@socketio.on("disconnect")
def disconnect():
    """
    Disconnect the interactive board.
    """
    local_sid = ""
    for key in interactive_screens.keys():
        if interactive_screens[key] == request.sid:
            local_sid = key
            break
    del interactive_screens[local_sid]
    print(f"disconnect {request.sid}")


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000, threaded=True)
