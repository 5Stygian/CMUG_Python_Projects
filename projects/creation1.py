# This should draw the logo for "The Good Work" by HarryBlank (roughly).

from cmu_graphics import *

from math import sin, cos, radians
from typing import Tuple, Dict

import os

os.system("clear")

# Variables
white: str = 'white'
black: str = 'black'
red: str   = 'red'

# Types
## Used for readability
## Short for "Coordinate"
Coord = Tuple[int, int]

## Short for "Coordinate Specification"
CoordSpec = Dict[str, Dict[str, int]]

# Functions
def rotate(x: int, y: int, degrees: int, xo=200, yo=200) -> Coord:
    rads: float = radians(-degrees)

    tx: float = x - xo
    ty: float = y - yo

    rx: float = tx*cos(rads) - ty*sin(rads)
    ry: float = tx*sin(rads) + ty*cos(rads)

    fx: float = rx + xo
    fy: float = ry + yo

    return (int(fx),int(fy))

def translatePoint(x: int, y: int, distx: int, disty: int) -> Coord:
    x += distx
    y += disty

    return (x,y)

#**********************************#
#**********************************#
#**********************************#

def redrawAll(app):
    # Main clircle
    mainCircle: Circle = drawCircle(
        200,200, # x,y
        200,     # radius
        fill=gradient('white','red'),
        border=black,
        borderWidth=25
    )

    # Inner circle
    innerCircle: Circle = drawCircle(
        200,200,
        165,
        fill=None,
        border=black,
        borderWidth=12
    )

    # SCP Motif
    mdims: CoordSpec = {
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

    SCPMotifTopBorder: Polygon = drawPolygon(
        mdims['bd1']['x'],mdims['bd1']['y'],
        mdims['bd2']['x'],mdims['bd2']['y'],
        mdims['bd3']['x'],mdims['bd3']['y'],
        mdims['bd4']['x'],mdims['bd4']['y']
    )
    SCPMotifTopBG: Polygon = drawPolygon(
        mdims['bg1']['x'],mdims['bg1']['y'],
        mdims['bg2']['x'],mdims['bg2']['y'],
        mdims['bg3']['x'],mdims['bg3']['y'],
        mdims['bg4']['x'],mdims['bg4']['y'],
        fill=gradient(red, rgb(245,60,70), start='top')
    )

    SCPMotifLeftBorder: Polygon = drawPolygon( # UNPACKING OPERATOR RAHHH
        *rotate(mdims['bd1']['x'], mdims['bd1']['y'], 120),
        *rotate(mdims['bd2']['x'], mdims['bd2']['y'], 120),
        *rotate(mdims['bd3']['x'], mdims['bd3']['y'], 120),
        *rotate(mdims['bd4']['x'], mdims['bd4']['y'], 120)
    )
    SCPMotifLeftBG: Polygon = drawPolygon(
        *rotate(mdims['bg1']['x'], mdims['bg1']['y'], 120),
        *rotate(mdims['bg2']['x'], mdims['bg2']['y'], 120),
        *rotate(mdims['bg3']['x'], mdims['bg3']['y']+1, 120),
        *rotate(mdims['bg4']['x'], mdims['bg4']['y']+2, 120),
        fill=gradient(red, rgb(245,60,70), start='left')
    )

    SCPMotifRightBorder: Polygon = drawPolygon(
        *rotate(mdims['bd1']['x'], mdims['bd1']['y'], 240),
        *rotate(mdims['bd2']['x'], mdims['bd2']['y'], 240),
        *rotate(mdims['bd3']['x'], mdims['bd3']['y'], 240),
        *rotate(mdims['bd4']['x'], mdims['bd4']['y'], 240)
    )
    SCPMotifRightBG: Polygon = drawPolygon(
        *rotate(mdims['bg1']['x'], mdims['bg1']['y'], 240),
        *rotate(mdims['bg2']['x'], mdims['bg2']['y'], 240),
        *rotate(mdims['bg3']['x'], mdims['bg3']['y']+1, 240),
        *rotate(mdims['bg4']['x'], mdims['bg4']['y']+2, 240),
        fill=gradient(red, rgb(245,60,70), start='right')
    )

    # Lightning bolt
    LBTop: Polygon = drawPolygon(
        230,75,
        155,190,
        210,220
    )

    LBBottom: Polygon = drawPolygon(
        175,330,
        245,195,
        190,165
    )

    # Arrow
    arrowhead: Polygon = drawPolygon(
        85,116,
        100,140,
        115,120
    )

    shaft: Line = drawLine(
        260,226,
        105,129,
        lineWidth=6
    )

    invertedShaft: Line = drawLine(
        237,211,
        168,168,
        fill=white,
        lineWidth=6
    )

    fdims: CoordSpec = {
        'bb1': {
            'x': 257,
            'y': 223
        },
        'bb2': {
            'x': 260,
            'y': 247
        },

        'bt1': {
            'x': 257,
            'y': 223
        },
        'bt2': {
            'x': 280,
            'y': 220
        }
    }

    feather1Bottom: Line = drawLine(
        fdims['bb1']['x'],fdims['bb1']['y'],
        fdims['bb2']['x'],fdims['bb2']['y'],
        lineWidth=6
    )
    feather1Top: Line = drawLine(
        fdims['bt1']['x'],fdims['bt1']['y'],
        fdims['bt2']['x'],fdims['bt2']['y'],
        lineWidth=6
    )

    feather2Bottom: Line = drawLine(
        *translatePoint(fdims['bb1']['x'],fdims['bb1']['y']-1, 14,9),
        *translatePoint(fdims['bb2']['x'],fdims['bb2']['y']-1, 14,9),
        lineWidth=6
    )
    feather2Top: Line = drawLine(
        *translatePoint(fdims['bt1']['x'],fdims['bt1']['y']+1, 14,9),
        *translatePoint(fdims['bt2']['x'],fdims['bt2']['y']+1, 14,9),
        lineWidth=6
    )

    feather3Bottom: Line = drawLine(
        *translatePoint(fdims['bb1']['x'],fdims['bb1']['y']-1, 28,18),
        *translatePoint(fdims['bb2']['x'],fdims['bb2']['y']-1, 28,18),
        lineWidth=6
    )
    feather3Top: Line = drawLine(
        *translatePoint(fdims['bt1']['x'],fdims['bt1']['y']+1, 28,18),
        *translatePoint(fdims['bt2']['x'],fdims['bt2']['y']+1, 28,18),
        lineWidth=6
    )

app.title = 'The Good Work'

runApp(
    width=400,
    height=400
)
