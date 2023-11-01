class InteractiveBoard {
  constructor(refreshRate = 100, displayDuration = 5000) {
    let that = this;
    this.socket = io();

    this.refreshRate = refreshRate;
    this.displayDuration = displayDuration;

    that.socket.on("connect", () => {
      console.log("Connected ", that.socket.connected);

      that.activeShapes = [new Map(), new Map()];
      that.canvas = [
        document.getElementById("canvas1"),
        document.getElementById("canvas2"),
      ];
      that.ctx = [
        that.canvas[0].getContext("2d"),
        that.canvas[1].getContext("2d"),
      ];
    });

    that.socket.on("sessionID", (sessionID) => {
      let elem = document.getElementById("sessionID");
      elem.textContent = `(id : ${sessionID})`;
      that.start();
    });

    this.socket.on("draw", (shape) => this.addShape(shape, 0));
    this.socket.on("draw/1", (shape) => this.addShape(shape, 0));
    this.socket.on("draw/2", (shape) => this.addShape(shape, 1));
  }

  start() {
    setInterval(() => this.redraw(), this.refreshRate);
  }

  redraw() {
    for (let i = 0; i < 2; i++) {
      this.ctx[i].clearRect(0, 0, this.canvas[i].width, this.canvas[i].height);
      for (const [key, value] of this.activeShapes[i]) {
        this.drawShape(this.ctx[i], value);
      }
    }
  }

  addShape(shape, canvasID) {
    console.log(shape);
    // Generate unique id for the shape
    let id = Math.floor(Math.random() * 100000000);

    // Add the shape to the drawing
    this.activeShapes[canvasID].set(id, shape);

    // Remove 5 secondes later
    setTimeout(() => {
      this.activeShapes[canvasID].delete(id);
    }, this.displayDuration);
  }

  drawShape(ctx, shape) {
    let rgbColor = `rgb(${shape.color[0]},${shape.color[1]},${shape.color[2]})`;
    ctx.fillStyle = rgbColor;
    switch (shape.shape) {
      case "rectangle":
        ctx.fillRect(shape.x, shape.y, shape.width, shape.height);
        break;
      case "square":
        ctx.fillRect(shape.x, shape.y, shape.cote, shape.cote);
        break;
      case "circle":
        ctx.beginPath();
        ctx.arc(shape.x, shape.y, shape.radius, 0, 2 * Math.PI, false);
        ctx.fill();
        break;
      case "point":
        ctx.arc(shape.x, shape.y, 5, 0, 2 * Math.PI, false);
        ctx.fill();
        break;
      case "line":
        drawLine(ctx, shape.x1, shape.y1, shape.x2, shape.y2, rgbColor);
        break;
      default:
        break;
    }
  }

  drawLine(ctx, x1, y1, x2, y2, stroke = "black", width = 5) {
    // start a new path
    ctx.beginPath();
    // place the cursor from the point the line should be started
    ctx.moveTo(x1, y1);
    // draw a line from current cursor position to the provided x,y coordinate
    ctx.lineTo(x2, y2);
    // set strokecolor
    ctx.strokeStyle = stroke;
    // set lineWidht
    ctx.lineWidth = width;
    // add stroke to the line
    ctx.stroke();
  }
}
