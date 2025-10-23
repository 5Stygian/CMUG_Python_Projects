from cmu_graphics import Polygon, Label, Group, rgb

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
                bgFill = rgb(200,200,200), bgBorder = rgb(180,180,180), bgBorderWidth = 2, bgVisible: bool = True,
                textFill = rgb(80,80,80), textFont: str = "arial", bold: bool = False, italic: bool = False, textVisible: bool = True):
        
        self.textContent = textContent
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        self.bgFill          = bgFill
        self.bgBorder        = bgBorder
        self.bgBorderWidth   = bgBorderWidth
        self.bgVisible       = bgVisible
        
        self.textFill        = textFill
        self.textFont        = textFont
        self.bold            = bold
        self.italic          = italic
        self.textVisible     = bgVisible
        
        self.background = Polygon(
            self.x1,self.y1,
            self.x2,self.y1,
            self.x2,self.y2,
            self.x1,self.y2,
            fill=self.bgFill,
            border=self.bgBorder,
            borderWidth=self.bgBorderWidth,
            visible=self.bgVisible
        )
        
        self.text = Label(
            self.textContent,
            self.background.centerX,self.background.centerY,
            fill=self.textFill,
            font=self.textFont,
            bold=self.bold,
            italic=self.italic,
            visible=self.textVisible
        )
    
        self.buttonGroup = Group( self.background, self.text )
        self.buttonGroup.tl = [self.background.x1, self.background.y1]
        self.buttonGroup.tr = [self.background.x2, self.background.y1]
        self.buttonGroup.bl = [self.background.x1, self.background.y2]
        self.buttonGroup.br = [self.background.x2, self.background.y2]
        
    # Only call when any of these attributes get changed
    def __updateAttrs(self) -> None:
        self.buttonGroup.tl = [self.background.x1, self.background.y1]
        self.buttonGroup.tr = [self.background.x2, self.background.y1]
        self.buttonGroup.bl = [self.background.x1, self.background.y2]
        self.buttonGroup.br = [self.background.x2, self.background.y2]
       
    def getGroup(self) -> Group:
        return self.buttonGroup.children
        
    def getData(self) -> Dict:
        returnDict = {
            "ClassName": self.__name__,
            "Dimensions": {
                "topLeft": self.buttonGroup.tl,
                "topRight": self.buttonGroup.tr,
                "bottomLeft": self.buttonGroup.bl,
                "bottomRight": self.buttonGroup.br
            },
            "Background": {
                "BackgroundFill": [self.bgFill.red,self.bgFill.green,self.bgFill.blue],
                "BorderFill": [self.bgBorder.red,self.bgBorder.green,self.bgBorder.blue],
                "BorderWidth": self.bgBorderWidth,
                "IsVisible": self.bgVisible
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
               xo: int|float = None, 
               yo: int|float = None) -> Tuple:
        
        # set local variables
        radians: float = rads(-degrees)
        if xo == None: xo = self.buttonGroup.centerX
        if yo == None: yo = self.buttonGroup.centerY
        
        # translate to origin
        self.background.x1 -= xo
        self.background.y1 -= yo
        
        self.background.x2 -= xo
        self.background.y2 -= yo
        
        self.background.x3 -= xo
        self.background.y3 -= yo
        
        self.background.x4 -= xo
        self.background.y4 -= yo
        
        # rotate around origin
        self.background.x1 = self.background.x1*cos(radians) - self.background.y1*sin(radians)
        self.background.y1 = self.background.x1*sin(radians) + self.background.y1*cos(radians)
        
        self.background.x2 = self.background.x2*cos(radians) - self.background.y2*sin(radians)
        self.background.y2 = self.background.x2*sin(radians) + self.background.y2*cos(radians)
        
        self.background.x3 = self.background.x3*cos(radians) - self.background.y3*sin(radians)
        self.background.y3 = self.background.x3*sin(radians) + self.background.y3*cos(radians)
        
        self.background.x4 = self.background.x4*cos(radians) - self.background.y4*sin(radians)
        self.background.y4 = self.background.x4*sin(radians) + self.background.y4*cos(radians)
        
        # translate back to original position
        self.background.x1 += xo
        self.background.y1 += yo
        
        self.background.x2 += xo
        self.background.y2 += yo
        
        self.background.x3 += xo
        self.background.y3 += yo
        
        self.background.x4 += xo
        self.background.y4 += yo
        
        self.__updateAttrs()
        
        return (
            (self.background.x1,self.background.y1),
            (self.background.x2,self.background.y2),
            (self.background.x3,self.background.y3),
            (self.background.x4,self.background.y4)
        )
        
        
# tests
if __name__ == "__main__":
    testButton = Button(
        "test",
        50,50,
        100,80
    )
    print(testButton.getGroup())
    print(testButton.getData())
    
    testButton.translate(100,100)
    print(testButton.getGroup())
    print(testButton.getData(), "\n")
    
    testButton.rotate(90)
    print(testButton.getGroup())
    print(testButton.getData())

    cmu_grapics.run()
