#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:10:33 2020

@author: Dr Z & Class

Note: Sound libraries may need updating.
"""

import random
import turtle
#import winsound
from pydub.playback import _play_with_simpleaudio as Play
from pydub import AudioSegment

turtle.colormode(255)

#Create a panel to draw on. 
setup()
panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#========================MAKE VARIABLES=======================
'''
Create a button using click interactions in turtle
Download a sound
Change the turtle to a square shape
Create a callback function that will play a sound
Use the onclick() method to turn the button into a sound playing button!
'''
# Set up panel
turtle.setup()
panel.bgcolor('blue')

# Get sound(s)
sound1 = AudioSegment.from_wav('tech.wav') #make sure command matches file type

# Set up turtle for the button
button = turtle.Turtle(shape='square')
size = 10
style = ('Courier', 30, 'italic')

# Set up button features
button.shapesize(size)
button.color('black','magenta')
button.up()
button.goto(300,300)
button.stamp() # make the box

# Add the text so users know what the button does
button.write('Play', font=style, align='center')
button.ht() #hide the turtle

def playSound(x,y):
    # callback function to play sound
    btnX = button.xcor()
    btnY = button.ycor()
    # make sure the click happens inside the button
    if btnX-round(size*10) < x < btnX+round(size*10) and btnY-round(size*10) < y < btnY+round(size*10):
        print(x,y)
        Play(sound1) # play sound in background
    
##Play the sound!
turtle.onscreenclick(playSound)
#listen for the clicks (panel.mainloop also works!)
turtle.listen()

turtle.done()