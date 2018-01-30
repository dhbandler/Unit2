#Daniel
#1/30/18
#coloredSquare.py makes a square of a certain color pop out

from random import randint
from ggame import *

num=randint(1,4)

if num==1:
    red=Color(0xFF0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)
    
    Sprite(rectangle)
    myApp=App()
    myApp.run()

elif num==2:
    blue=Color(0x0000FF,1)
    line=LineStyle(3,blue)
    rectangle=RectangleAsset(100,100,line,blue)
    
    Sprite(rectangle)
    myApp=App()
    myApp.run()
    
elif num==3:
    yellow=Color(0xFFFF00,1)
    line=LineStyle(3,yellow)
    rectangle=RectangleAsset(100,100,line,yellow)
    
    Sprite(rectangle)
    myApp=App()
    myApp.run()
elif num==4:
    green=Color(0x008000,1)
    line=LineStyle(3,green)
    rectangle=RectangleAsset(100,100,line,green)
    
    Sprite(rectangle)
    myApp=App()
    myApp.run()
    
