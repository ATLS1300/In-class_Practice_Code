#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:47:35 2020

@author: Dr Z
draws colorful circles when clicking
"""

import random
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
panel.setup(width=w, height=h) #
panel.setworldcoordinates(0, w, h, 0)

def Rainbow(x,y):
    rainTurt = []
    tracer(9)
    for i in range(6): #create list of turtles
        rainTurt.append(Turtle(visible=False, shape='circle'))
        colormode(255)
        rainTurt[-1].up()
        rainTurt[-1].color('black',rainbow[i])
        rainTurt[-1].shapesize(random.randint(1,2))
        rainTurt[-1].seth(random.randint(0,360))
        rainTurt[i].goto(x,y)
    update()
    #animate them
    dist = random.randint(10,50)
    for i in range(len(rainTurt)):
        rainTurt[i].showturtle()
        rainTurt[i].forward(dist)
        rainTurt[i].stamp()

panel.clear()

w = 600 # width of panel
h = 600 # height of panel

rainbow = [(228,3,3),(255,140,0),(255,237,0),(0,128,38),(0,77,255),(117,7,135)]

panel.onclick(Rainbow)

panel.mainloop()

done()  