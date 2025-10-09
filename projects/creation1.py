# This should draw the logo for "The Good Work" by HarryBlank. 

from cmu_graphics import *

black: str = 'black'
red: str   = 'red'

# Main clircle
mainCircle: Circle = Circle(
    200,200, # x,y
    200,     # radius
    fill=gradient('white','red'),
    border=black,
    borderWidth=25
)

# Inner circle
innerCircle: Circle = Circle(
    200,200,
    165,
    fill=None,
    border=black,
    borderWidth=12
)

# SCP motif
def SCPMotif():
    SCPMotifTopBorder: Polygon = Polygon(
        175,20,
        225,20,
        225,48,
        175,48,
        border=black,
        borderWidth=12
    )
    SCPMotifTopBG: Polygon = Polygon(
        185,25,
        215,25,
        215,48,
        185,48,
        fill=red
    )

SCPMotif()