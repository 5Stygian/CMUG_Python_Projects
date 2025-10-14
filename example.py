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