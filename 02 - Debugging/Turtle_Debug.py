'''
Turtle starter code
ATLS 1300
Author: Dr. Z
May 29, 2020
'''
import math, random
import turtle #import the library of commands that you'd like to use
turtle.colormode(255)

#Create a panel to draw on. 
panel = turtle.Screen()
panel.clear()
w = 720 # width of panel
h = 720 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

panel.bgcolor('gray')

color = ['red','white']

square = turtle.Turtle()
square.color(color[0],color[1])
size = 200

square.up()
square.goto(40.0,30.5)
square.down()

square.begin_fill()
square.circle(size)
square.end_fill()
square.rihgt(21)

turtle.begin_fill()
square.circle("size")
turtle.end_fill()
    
    