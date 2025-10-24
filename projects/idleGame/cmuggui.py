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

class Menu:
    def __init__(self, x1: int|float|None = None, y1: int|float|None = None, x2: int|float|None = None, y2: int|float|None = None,
                position: str = "custom",
                bbFill = "lightgray", bbBorder = "gray", bbBorderWidth: int|float = 2):
        
        self.position = position
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        self.bbFill        = bbFill
        self.bbBorder      = bbBorder
        self.bbBorderWidth = bbBorderWidth
        
        self.buttonAmount = 1
        self.buttons = { "Buttons": {} }
        
        match self.position:
            case "custom":
                self.boundingBox = Polygon(
                    self.x1,self.y1,
                    self.x2,self.y1,
                    self.x2,self.y2,
                    self.x1,self.y2,
                    fill=self.bbFill,
                    border=self.bbBorder,
                    borderWidth=self.bbBorderWidth
                )
            case "left":
                self.boundingBox = Polygon(
                    0,0,
                    app.width/2.3,0,
                    app.width/2.3,app.height,
                    0,app.height,
                    fill=self.bbFill,
                    border=self.bbBorder,
                    borderWidth=self.bbBorderWidth
                )
            case "right":
                self.boundingBox = Polygon(
                    app.width,0,
                    app.width-app.width/2.3,0,
                    app.width-app.width/2.3,app.height,
                    app.width,app.height,
                    fill=self.bbFill,
                    border=self.bbBorder,
                    borderWidth=self.bbBorderWidth
                )
            case "center":
                self.boundingBox = Polygon(
                    app.width/4,app.height/4,
                    app.width/1.333,app.height/4,
                    app.width/1.333,app.height/1.333,
                    app.width/4,app.height/1.333,
                    fill=self.bbFill,
                    border=self.bbBorder,
                    borderWidth=self.bbBorderWidth
                )
        
        self.menu = {
            "Menu": {
                "BoundingBox": {
                    "Position": {
                        "TopLeft": [self.boundingBox.left,self.boundingBox.top],
                        "TopRight": [self.boundingBox.right,self.boundingBox.top],
                        "BottomLeft": [self.boundingBox.left,self.boundingBox.bottom],
                        "BottomRight": [self.boundingBox.right,self.boundingBox.bottom],
                        "Center": [self.boundingBox.centerX,self.boundingBox.centerY],
                    },
                    "Color": self.boundingBox.fill,
                    "BorderColor": self.boundingBox.border,
                    "BorderWidth": self.boundingBox.borderWidth,
                    "IsVisible": self.boundingBox.visible
                }
            }
        }
        self.menuGroup = Group( self.boundingBox )

    def addButton(self, text, ydistance: int|float = 1.0):
        self.buttonBoundingBox = Rect(
            self.boundingBox.centerX/2,(40*self.buttonAmount*ydistance),
            100,25,
            fill="white"
        )
        self.buttonLabel = Label(
            text,
            self.buttonBoundingBox.centerX,self.buttonBoundingBox.centerY
        )
        
        localButtonGroup = Group( self.buttonBoundingBox, self.buttonLabel )
        
        updatedButtonData = self.buttons["Buttons"].update({
            f"Button_{self.buttonAmount}": {
                "Index": self.buttonAmount,
                "BoundingBox": {
                    "Position": {
                        "TopLeft": [self.buttonBoundingBox.left,self.buttonBoundingBox.top],
                        "TopRight": [self.buttonBoundingBox.right,self.buttonBoundingBox.top],
                        "BottomLeft": [self.buttonBoundingBox.left,self.buttonBoundingBox.bottom],
                        "BottomRight": [self.buttonBoundingBox.right,self.buttonBoundingBox.bottom],
                        "Center": [self.buttonBoundingBox.centerX,self.buttonBoundingBox.centerY],
                    },
                    "Color": self.buttonBoundingBox.fill,
                    "BorderColor": self.buttonBoundingBox.border,
                    "BorderWidth": self.buttonBoundingBox.borderWidth,
                    "IsVisible": self.buttonBoundingBox.visible
                },
                "Text": {
                    "Position": [self.buttonLabel.centerX,self.buttonLabel.centerY],
                    "Value": self.buttonLabel.value,
                    "Color": self.buttonLabel.fill,
                    "Font": self.buttonLabel.font,
                    "IsBold": self.buttonLabel.bold,
                    "IsItalic": self.buttonLabel.italic,
                    "IsVisible": self.buttonLabel.visible
                }
            }
        })
        
        self.buttonAmount += 1
        
        self.menuGroup.toBack()

    def getMenus(self):
        return self.menu

    def getButtons(self, getIndexed: bool = False, index: int = 1):
        if getIndexed == False:
            return self.buttons
        elif getIndexed == True:
            return self.buttons[f"Button_{index}"]
    
    def getData(self):
        return self.menu|self.buttons

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
    testMenu = Menu(
        position="left"
    )
    testMenu.addButton("test")
    testMenu.addButton("test2")
    pp(testMenu.getData(), sort_keys=False, indent=4)

    '''testButton = Button(
        "test",
        0,0,
        30,20
    )
    pp(testButton.getData(), sort_keys=False)'''

    '''testButton.translate(100,100)
    pp(testButton.getData(), sort_keys=False)

    testButton.rotate(90)
    pp(testButton.getData(), sort_keys=False)'''

    cmu_graphics.run() # type: ignore
