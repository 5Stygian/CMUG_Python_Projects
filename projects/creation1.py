# This should draw the logo for "The Good Work" by HarryBlank. 

from cmu_graphics import *

from math import sqrt
from typing import List

black: str = 'black'
red: str   = 'red'

# Functions
def r120(x: float, y: float) -> List[float]:
    x = -0.5*x - (sqrt(3)/2)*y
    y = -0.5*y - (sqrt(3)/2)*x
    return [x,y]

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
def SCPMotif(
    x1: int, y1: int,
    x2: int, y2: int,
    x3: int, y3: int,
    x4: int, y4: int
) -> None:
    SCPMotifTopBorder: Polygon = Polygon(
        x1,y1,
        x2,y2,
        x3,y3,
        x4,y4,
        border=black,
        borderWidth=12
    )
    SCPMotifTopBG: Polygon = Polygon(
        x1+10,y1+5,
        x2-10,y2+5,
        x3-10,y3,
        x4+10,y4,
        fill=red
    )
    
    x1,y1 = r120(x1,y1) # do ts for all of them
    
    SCPMotifRightBorder: Polygon = Polygon(
        x1,y1,
        x2,y2,
        x3,y3,
        x4,y4,
        border=black,
        borderWidth=12
    )

SCPMotif(175,20, 225,20, 225,48, 175,48)

'''SCPMotifTopBorder: Polygon = Polygon(
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
)'''