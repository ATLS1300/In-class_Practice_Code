'''
Turtle starter code
ATLS 1300
Author: Dr. Z
May 29, 2020
'''
import math, random
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
panel.clear()
w = 720 # width of panel
h = 720 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)
panel.bgcolor('gray')

Color = ['red','white']

square = Turtle()
square.color(color[0],color[2])
size = 200
sides = 4
angle = 360/4

square.up()
square.goto(400.0,300)
square.down()

for i in range(300):
    begin_fill()
    for sides in range(4):
        square.forward(size)
        square.right(angle)
    square.rihgt(21)
    end_fill()