#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:16:24 2020

@author: master
"""

import turtle

panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0)    

class Button: # create a class for my button
    def __init__(self, size,x,y,screen=panel,lineColor='black',fillColor='magenta',filename=None): 
        # define attributes, these will be the variables from my button script
        if filename: # only load the sound if filename has a value
            self.sound = sa.WaveObject.from_wave_file(filename) #this will change based on your sound component
        self.size = size
        self.x = x
        self.y = y
        self.lineColor = lineColor
        self.fillColor = fillColor
        self.startColor = fillColor

#        # Now let's make the turtle object
        self.Btn = turtle.Turtle()
        self.makeBtnImg() # you can call a method inside the init funciton, and 
#        # it will automatically run that method when you instantiate your object
#        self.imgBtn.onclick(self.changeColor)  # starts onclick detection when object is made.

        
# When I made my button, I set up all the features. This should make a nice method.
    def makeBtnImg(self): # again, I don't know what my parameters will be...
        self.Btn.shape('square')
        self.Btn.shapesize(self.size)
        self.Btn.pensize(10)
        self.Btn.color(self.lineColor,self.fillColor) # values in the class
        self.Btn.up()
        self.Btn.goto(self.x,self.y) #values in the class
        self.Btn.down()
        self.Btn.stamp() # make the box    
        
class Opponent(Button):
    def __init__(self,color2='blue'):
        super(Opponent,self).__init__(5,200,100,fillColor=color2)
        self.color2 = color2
        self.makeBtnImg()
        
    def spin(self):
        self.Btn.right(180)
        
        
firstBtn=Button(5,100,100)
oppBtn = Opponent('yellow')
        
oppBtn.spin()
        
        
        