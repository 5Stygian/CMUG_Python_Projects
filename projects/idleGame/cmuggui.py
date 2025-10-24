from cmu_graphics import *
from beeprint import pp

from dataclasses import dataclass
from typing import Dict, Tuple
from math import sin, cos
from math import radians as rads

@dataclass
class Colors:
    gray         = rgb(175,175,175)
    darkGray     = rgb(100,100,100)
    darkerGray   = rgb(80,80,80)
    darkererGray = rgb(40,40,40)

class Button:
    def __init__(self, textContent: str,
                x1: int|float, y1: int|float, x2: int|float, y2: int|float,
                hbFill = rgb(200,200,200), hbBorder = rgb(180,180,180), hbBorderWidth = 2, hbVisible: bool = True,
                textFill = rgb(80,80,80), textFont: str = "arial", bold: bool = False, italic: bool = False, textVisible: bool = True):

        self.textContent = textContent

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.hbFill          = hbFill
        self.hbBorder        = hbBorder
        self.hbBorderWidth   = hbBorderWidth
        self.hbVisible       = hbVisible

        self.textFill        = textFill
        self.textFont        = textFont
        self.bold            = bold
        self.italic          = italic
        self.textVisible     = textVisible

        self.hitbox = Polygon(
            self.x1,self.y1,
            self.x2,self.y1,
            self.x2,self.y2,
            self.x1,self.y2,
            fill=self.hbFill,
            border=self.hbBorder,
            borderWidth=self.hbBorderWidth,
            visible=self.hbVisible
        )

        self.text = Label(
            self.textContent,
            self.hitbox.centerX,self.hitbox.centerY,
            fill=self.textFill,
            font=self.textFont,
            bold=self.bold,
            italic=self.italic,
            visible=self.textVisible
        )

        self.buttonGroup = Group( self.hitbox, self.text )
        self.buttonGroup.tl = [self.hitbox.x1, self.hitbox.y1]
        self.buttonGroup.tr = [self.hitbox.x2, self.hitbox.y2]
        self.buttonGroup.bl = [self.hitbox.x3, self.hitbox.y3]
        self.buttonGroup.br = [self.hitbox.x4, self.hitbox.y4]

    # Only call when any of these attributes get changed
    def __updateAttrs(self) -> None:
        self.buttonGroup.tl = [self.hitbox.x1, self.hitbox.y1]
        self.buttonGroup.tr = [self.hitbox.x2, self.hitbox.y2]
        self.buttonGroup.bl = [self.hitbox.x3, self.hitbox.y3]
        self.buttonGroup.br = [self.hitbox.x4, self.hitbox.y4]

    def getGroup(self) -> Group:
        return self.buttonGroup.children

    def getData(self) -> Dict:
        returnDict = {
            "ClassName": self.__class__.__name__,
            "Group": f"{self.buttonGroup.children}",
            "Hitbox": {
                "Dimensions": {
                    "TopLeft": self.buttonGroup.tl,
                    "TopRight": self.buttonGroup.tr,
                    "BottomLeft": self.buttonGroup.bl,
                    "BottomRight": self.buttonGroup.br
                },
                "BackgroundFill": [self.hbFill.red,self.hbFill.green,self.hbFill.blue],
                "BorderFill": [self.hbBorder.red,self.hbBorder.green,self.hbBorder.blue],
                "BorderWidth": self.hbBorderWidth,
                "IsVisible": self.hbVisible
            },
            "Text": {
                "TextContent": self.text.value,
                "TextPosition": [self.text.centerX, self.text.centerY],
                "TextSize": self.text.size,
                "TextFill": [self.text.fill.red,self.text.fill.green,self.text.fill.blue],
                "TextFont": self.text.font,
                "IsBold": self.text.bold,
                "IsItalic": self.text.italic,
                "IsVisible": self.textVisible
            }
        }
        return returnDict

    def translate(self, x: int|float, y: int|float) -> Tuple:
        self.buttonGroup.centerX += x
        self.buttonGroup.centerY += y
        self.__updateAttrs()
        return (x, y)

    def rotate(self, degrees: int|float,
               xo: int|float|None = None,
               yo: int|float|None = None) -> Tuple:

        # set local variables
        if xo == None: xo = self.buttonGroup.centerX
        if yo == None: yo = self.buttonGroup.centerY

        self.hitbox.rotate(degrees, xo, yo)
        self.text.rotate(degrees, xo, yo)

        self.__updateAttrs()

        return (
            (self.hitbox.x1,self.hitbox.y1),
            (self.hitbox.x2,self.hitbox.y2),
            (self.hitbox.x3,self.hitbox.y3),
            (self.hitbox.x4,self.hitbox.y4)
        )


# tests
if __name__ == "__main__":
    testButton = Button(
        "test",
        0,0,
        30,20
    )
    pp(testButton.getData(), sort_keys=False)

    testButton.translate(100,100)
    pp(testButton.getData(), sort_keys=False)

    testButton.rotate(90)
    pp(testButton.getData(), sort_keys=False)

    cmu_graphics.run() # type: ignore
