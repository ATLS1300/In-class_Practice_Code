
"""
Created on Mon Feb 10 11:23:01 2020

@author: mallorybenna
This code creates a pygame display that moves with key strokes 
(up, down, left, right arrows)
This code is modified from a pygame tutorial: https://www.youtube.com/watch?v=i6xMBig-pP4
"""

#Importing pygame (having trouble with some of these imports and have to restart kernel)
import pygame
from pygame.draw import *
from pygame.locals import *

#initializing screen
pygame.init() #start the pygame module running in the background
#This line is needed to use most pygame functions!

size = [500,500] #screen size, width, height (pixels)
screen = pygame.display.set_mode(size) #create the window
pygame.display.set_caption("Example") #give the window a title

#Setting variables for rectangle
x = 50
y = 50
width = 40
height = 60
vel = 5

#Set controls for while loop
run = True #set initial condition for 
mouseOver = False #set initial condition for mouse detection
(255,0,0) = Color #rgb value for shape color (red). Notice that it's 0-255 (not 0-1)


#Control action
while run:
    #this while loop continues until there's something goes wrong, or a conditional
    # conditional, such as an if statement (line 44), returns a False 
    # since run is set to True, the while loop continues. If we quit the pygame
    # window, run gets turned to false (lines 44-45), and the loop stops.
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        #for all the user events (keystroke, mouse click, etc) that pygame
        #can detect, do the following
        if event.type == pygame.QUIT:
            #use an if statement to check if the event that is detect is a click
            #to close the window
            run = False #if it is, then run becomes false, and the while loop stops.
        
        #If you press space, change color of the rectangle
        if (event.type == pygame.KEYDOWN) and (event.key == K_SPACE):
            #use an if statement to check to see if the user has clicked a keybaord
            #button AND ALSO if that keyboard key is a space bar
            Color = (0,255,0) #then turn the color value to  blue. Hint: where does blue get used?
    
    #Moving on in our loop...
    
    #Changing movement by key strokes
    keys = pygame.key.get_pressed() #look for user key presses, and save them to the variable, keys
    if keys[pygame.K_LEFT]:
        #pygame.K_[BTN] is a pygame library variable that stores the ASCII value,
        #which is the same as the key index (explore ASCII: https://www.w3.org/2002/09/tests/keys-cancel2.html)
        X -= vel #to move left, subtract a speed value from the x position
        
    if keys[pygame.K_RIGHT]:
        x += vel #to move right, add a speed value from the x position
    
    if keys[pygame.K_UP]:
        y -= vel #to move up, subtract a speed value to the y position
        
    if keys[pygame.K_DOWN]:
        y += vel #to move down, add a speed value to the y position
        
    #Fill screen and draw rectangle, and update
    screen.fill((0,0,0)) #redraw the screen before each movement of the rectangle, 
    #otherwise, there will be a trail
    pygame.draw.rect(screen,Color,(x,y,width,height)) #create a rectangle
    pygame.display.update() #update the display
    
            
pygame.quit() #when you leave the while loop, stop the pygame module from running in the background

