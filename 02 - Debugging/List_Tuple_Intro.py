#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:20:03 2022

@author: sazamore

List Practice

Make lists, append and index them
"""
# This is a list definition
names = ["Charles", "Logan", "Jean"]

# This list has 3 elements or values
# The len function lets you see the number of elements in the variable
print(len(names))

#===============INDEXING===============
# Let's practice indexing!

# Print the first value in the list


# Print the last value in the list

# What do you think the line below will print? 
# Guess and then uncomment to find out!
# print(names[-1])

# Indexing also let's us change values. 
# names[1]="Wolverine" # changes the second name to Wolverine

# try changing the third name to "Phoenix" using indexing

# print(names) # uncomment to check!
#===============APPENDING VALUES===============
# Let's change the list length

# Complete the line! Use the assign operater += to add "Scott"
names

print(names)

# now add ["Scott"] then print names. Note the difference!

# Lists also have built-in functions that you can access using
# dot notation. See what happens when you uncomment and run the code
# below

# names.append("Henry")

# names.append(value) does the same thing as names += [value]

#====================COLORS==============
# Let's make a list of colors. Define a variable called RAINBOWS
# this value should have all the colors of the rainbow as strings (ROYGBIV)

# Let's import turtle and use these values to change the color of the turtle
import turtle

rainbowTurtle = turtle.Turtle("Turtle") # makes a turtle shape

#use rainbowTurtle.color() and your RAINBOW variable to change the color
#you will have to index RAINBOW to get a specific color!



# set the color to red:

    
# set the color to green:

    
# set the color to violet:


# set the color to indigo using right hand indexing (negative values):

    
# change the value of indigo to "dark slate gray" using indexing


# paste the line from 73 without changing it and see what happens--the color should change even though the text didn't!
    

#====================ERRORS==============
# Now let's make some errors. Understanding how things break will make you a stronger programmer!

# Try to access an index that is NOT in RAINBOW. Use the index value 10.

# What error type did you get?


# Now let's work with tuples. We can change one variable type to another by using the name of the
# type as a function. We can change the list RAINBOW to a tuple by uncommenting the line below:

# Rainbow = tuple(RAINBOW)

# Tuples are immutable-you cannot change the values stored within them.
# Change the first value of Rainbow to "RED"

# What error type did you get?

