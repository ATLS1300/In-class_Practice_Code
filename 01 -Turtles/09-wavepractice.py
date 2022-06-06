#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 13:38:39 2020

@author: master
"""
import math
import turtle
turtle.colormode(255)

#Create a panel to draw on. 
panel = turtle.Screen()
panel.clear()
w = 720 # width of panel
h = 720 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================
# Let's use 2 turtles to draw waves and circles


wave1 = turtle.Turtle()
wave2 = turtle.Turtle()
startx = -200
starty = 200

wave1.color('green')
wave2.color('blue')

wave1.up()
wave2.up()

wave1.goto(startx, starty)
wave2.goto(startx, starty)

amp = 100 #change this value to change the height of your wave (amplitude)
scale = 1 #change this value to change the width of your wave (period)

#Draw a sine and cosine wave

for x in range(360):
    #Each iteration calculates ONE point on the wave
    rad = math.radians(x) #determines horizonal position
    y1 = amp * math.sin(rad) + 200  #determines vertical position for first wave
    y2 = amp * math.cos(rad) + 200  #determines vertical position for second wave
    wave1.down()
    wave2.down()
    wave1.goto((startx+x)*scale,y1)  #changing the x value will change the period of your wave
    wave2.goto((startx+x)/scale,y2)

#====================================
#Draw a circle

for x in range(360):
    #Each iteration calculates ONE point on the wave
    rad = math.radians(x) #determines horizonal position
    x1 = amp * math.sin(rad) + 200
    y1 = amp * math.cos(rad) + 200
    wave2.down()
    wave2.goto(x1+startx,y1)
wave2.up()


#====================================
# Draw multiple circles with a nested for loop   
 
numCirc = 5
centerx = 200 # center of our circle x coordinate
centery = 200 # center of our circle y coordinate

for circ in range(numCirc):    
    # make multiple circles
    for x in range(360):
        # make a single circle
        #Each iteration calculates ONE point on the wave
        rad = math.radians(x) #determines horizonal position
        x1 = amp/2 * math.sin(rad) + centerx # when x axis amp and y axis amp are unequal, you get an ellipse!
        y1 = amp * math.cos(rad) + centery
        wave2.down()
        wave2.goto(x1,y1)
    wave2.up()
    # Update the center of the circle
    centerx = circ*100
    centery = circ*100
        
turtle.done()