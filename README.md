# CMUG Python Projects

# CMUG Install Instructions
### Only tested on VSCode

- Install the CMU_Graphics lib from their website (https://academy.cs.cmu.edu/desktop)
- Move the folder titled "cmu_graphcis" into the directory with your python file that imports it
- - Don't forget to add it to your .gitignore!
- Make a .venv 
- Add "from cmu_graphics import *" to the top of the python file
- At the bottom of your file, add a function called "runApp()" with the keyword arguments "width" and "height". These will define the width and height of your window
- All of your code that will be drawn must be inside of a function called "redrawAll()". It takes a single argument, "app"
- All shape functions (Rect, Polygon, etc.) are replaced with "drawRect", "drawPolygon", etc.
- If your project throws an error that ends with an error about a module named 'pygame', run "pip install pygame" in the command line

This is an example of what your file should look like:
'''python

from cmu_graphics import *

def redrawAll(app):
    exampleShape: Rect = drawRect(
        100,100,
        100,100,
        fill=gradient('white','black', start='right')
    )

    exampleLabel: Label = drawLabel(
        'Jello, World!',
        120,350,
        size=41,
        fill='cornflowerBlue',
        font='arial'
    )

app.title = 'My Super Awesome Example Program'

runApp(
    width=400,
    height=400
)

'''