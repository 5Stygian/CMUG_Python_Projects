# This should draw the logo for "The Good Work" by HarryBlank. 

from cmu_graphics import *

from math import sqrt, sin, cos, radians
from typing import Tuple, Dict

black: str = 'black'
red: str   = 'red'

# Functions
def rotate(x, y, degrees, xo=200, yo=200) -> Tuple[int]:
    rads = radians(-degrees)
    
    tx = x - xo
    ty = y - yo
    
    rx = tx*cos(rads) - ty*sin(rads)
    ry = tx*sin(rads) + ty*cos(rads)
    
    fx = rx + xo
    fy = ry + yo
    
    return (int(fx),int(fy))

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

# SCP Motif
mdims: Dict[str, Dict[str,int]] = {
    'bd1': {
        'x': 170,
        'y': 20
    },
    'bd2': {
        'x': 230,
        'y': 20
    },
    'bd3': {
        'x': 230,
        'y': 48
    },
    'bd4': {
        'x': 170,
        'y': 48
    },
    
    'bg1': {
        'x': 180,
        'y': 25
    },
    'bg2': {
        'x': 220,
        'y': 25
    },
    'bg3': {
        'x': 220,
        'y': 48
    },
    'bg4': {
        'x': 180,
        'y': 48
    }
}

SCPMotifTopBorder: Polygon = Polygon(
    mdims['bd1']['x'],mdims['bd1']['y'],
    mdims['bd2']['x'],mdims['bd2']['y'],
    mdims['bd3']['x'],mdims['bd3']['y'],
    mdims['bd4']['x'],mdims['bd4']['y']
)
SCPMotifTopBG: Polygon = Polygon(
    mdims['bg1']['x'],mdims['bg1']['y'],
    mdims['bg2']['x'],mdims['bg2']['y'],
    mdims['bg3']['x'],mdims['bg3']['y'],
    mdims['bg4']['x'],mdims['bg4']['y'],
    fill=red
)

SCPMotifLeftBorder: Polygon = Polygon( # UNPACKING OPERATOR RAHHH
    *rotate(mdims['bd1']['x'], mdims['bd1']['y'], 120),
    *rotate(mdims['bd2']['x'], mdims['bd2']['y'], 120),
    *rotate(mdims['bd3']['x'], mdims['bd3']['y'], 120),
    *rotate(mdims['bd4']['x'], mdims['bd4']['y'], 120)
)
SCPMotifLeftBG: Polygon = Polygon(
    *rotate(mdims['bg1']['x'], mdims['bg1']['y'], 120),
    *rotate(mdims['bg2']['x'], mdims['bg2']['y'], 120),
    *rotate(mdims['bg3']['x'], mdims['bg3']['y']+1, 120),
    *rotate(mdims['bg4']['x'], mdims['bg4']['y']+2, 120),
    fill=red
)
   
SCPMotifRightBorder: Polygon = Polygon(
    *rotate(mdims['bd1']['x'], mdims['bd1']['y'], 240),
    *rotate(mdims['bd2']['x'], mdims['bd2']['y'], 240),
    *rotate(mdims['bd3']['x'], mdims['bd3']['y'], 240),
    *rotate(mdims['bd4']['x'], mdims['bd4']['y'], 240)
)
SCPMotifRightBG: Polygon = Polygon(
    *rotate(mdims['bg1']['x'], mdims['bg1']['y'], 240),
    *rotate(mdims['bg2']['x'], mdims['bg2']['y'], 240),
    *rotate(mdims['bg3']['x'], mdims['bg3']['y']+1, 240),
    *rotate(mdims['bg4']['x'], mdims['bg4']['y']+2, 240),
    fill=red
)
