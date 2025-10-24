from cmu_graphics import *

from assets import Colors, Button

import os

testButton = Button(
    100,100,
    200,200,
    "this is a test"
)

print(testButton.getGroup())

#*****************************#
#*****************************#
#*****************************#

os.system("clear")

app.title = "idleGame"

cmu_graphics.run() # type: ignore
