from cmu_graphics import Polygon, Label, Group, rgb

from dataclasses import dataclass

@dataclass
class Colors:
    gray         = rgb(175,175,175)
    darkGray     = rgb(100,100,100)
    darkerGray   = rgb(80,80,80)
    darkererGray = rgb(40,40,40)

class Button(Polygon):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, textContent: str,
                 backgroundFill=Colors.gray,
                 textFill=Colors.darkererGray, textFont="arial"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.backgroundFill = backgroundFill
        self.textContent    = textContent
        self.textFill       = textFill
        self.textFont       = textFont

        background = Polygon(
            self.x1,self.y1,
            self.x2,self.y2,
            fill=self.backgroundFill
        )

        text = Label(
            self.textContent,
            background.centerX,background.centerY,
            fill=self.textFill,
            font=self.textFont
        )

        self.spriteGroup = Group( background, text )
    
    def getGroup(self) -> Group:
        return self.spriteGroup