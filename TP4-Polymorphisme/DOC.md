# API tableau interactif

Pour afficher une forme sur le tableau interactif, nous réalisons des appels d'API comme suit: 

### Afficher un point
```
method: POST
endpoint: http://draw.david-albert.fr/draw/{displayID}
body (json): {"shape": "point", "x": 30, "y": 30, "color": (120, 200, 102)}
```

### Afficher une ligne
```
method: POST
endpoint: http://draw.david-albert.fr/draw/{displayID}
body (json): {"shape": "line", "x1": 30, "y1": 30, "x2": 60, "y2": 60, "color": (210, 110, 200)}
```

### Afficher un cercle
```
method: POST
endpoint: http://draw.david-albert.fr/draw/{displayID}
body (json): {"shape": "circle", "x": 40, "y": 40, "radius": 20, "color": (220, 140, 210)}
```

### Afficher un rectangle
```
method: POST
endpoint: http://draw.david-albert.fr/draw/{displayID}
body (json): {"shape": "rectangle", "x": 40, "y": 40, "width": 200, "height": 100, "color": (120, 220, 210)}
```

### Afficher un carré
```
method: POST
endpoint: http://draw.david-albert.fr/draw/{displayID}
body (json): {"shape": "square", "x": 30, "y": 30, "cote": 80, "color": (210, 110, 200)}
```
