---
marp: true
---

<style>
:root {
background-color:#FFF;
font-size: 10px;
}

</style>

<div class='mermaid'>
%%{init: {'theme': 'base',
'themeVariables': {
'primaryColor': '#fff',
'primaryTextColor': '#1f1b30',
'primaryBorderColor': '#FF2453',
'lineColor': '#1f1b30',
'secondaryColor': '#006100',
'tertiaryColor': '#fff',
'fontFamily':'verdana',
'fontSize':'200%'
}, 
'flowchart' : { 'curve' : 'basis' } 
} }%%
classDiagram 
direction TB
class GraphicalShape {
    #thicknessLine
    #ordinate
    #abscissa
    #color

    +move()
    +display()
    +rotate()

}

class ComposedGraphicalShape {
+display()
+rotate()
}

class Point {
+display()
+rotate()
}

class Circle {

-diameter
+display()
+rotate()

}

class Square {
-side

+display()
+rotate()
}

GraphicalShape <|-- Point
GraphicalShape <|-- Circle
GraphicalShape <|-- Square
GraphicalShape "1..\*" --\* ComposedGraphicalShape
GraphicalShape <|-- ComposedGraphicalShape

</div>
