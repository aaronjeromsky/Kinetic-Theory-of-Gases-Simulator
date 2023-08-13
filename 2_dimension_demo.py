import math
from random import random
from time import sleep
from tkinter import *
from particles import *

#TODO: create a ui so that the user can set some of these variables to whatever they want
#e.g. d, bounds, actual windowsize?, numBalls, maxRadius, genMaxVel, 

def display2DBalls():
        #TODO if we still use tKinter we need to not draw ovals on top of each other forever
        for i in range(numBalls):
            radius = balls[i].radius * pixelToUnitRatio
            posX = balls[i].pos[0] * pixelToUnitRatio
            posY = balls[i].pos[1] * pixelToUnitRatio
            canvas.create_oval(posX - radius, posY - radius, posX + radius, posY + radius, fill = balls[i].color)

#set up variables
sleepTime = 0.01  # Delay in seconds between frames
d = 2
bounds = [] # it will be a rectangle, rectangular prism, etc
sizes = []
for i in range(d):
    #this s makes a 1 by 1 box, but this should be something the user can change?
    #for now it's [[0, 1], [0, 1]]
     bounds.append([0, 1])
     sizes.append(abs(bounds[i][1] - bounds[i][0]))
width = sizes[0]
height = sizes[1]
pixelToUnitRatio = 500
pixelHeight = height * pixelToUnitRatio
pixelWidth = width * pixelToUnitRatio
leftSide = 0
rightSide = pixelWidth
numBalls = 50
balls = []
maxRadius = 1
genMaxVel = 1 #maximum velocity that will be generated

# Create the window and canvas
window = Tk()
window.title("Kinetic Theory of Gases Simulator")
window.resizable(False, False)
canvas = Canvas(window, width = pixelWidth, height = pixelHeight)
canvas.pack()

#get particles started
window.update # ? Is this helpful
generateBalls(balls, d, bounds, numBalls, maxRadius, genMaxVel)
display2DBalls() #display initial state

# main loop
while True:

    # Move
    for i in range(numBalls): # TODO: 

        #reverse velocity if a ball is out of bounds in any dimension
        for dim in range(d):
            if balls[i].pos[dim] + balls[i].radius > bounds[dim][1] or balls[i].pos[dim] - balls[i].radius < bounds[dim][0]: #would it be better to have a variable reference Ball[i]? idk
                balls[i].vel[dim] *= -1

        # * Should it move here too?
        # * This is occuring more often than it needs to be, but this may be useful later
        balls[i].pos[0] += balls[i].vel[0] * sleepTime  # pixels moved per tick.
        balls[i].pos[1] += balls[i].vel[1] * sleepTime

    sleep(sleepTime)

    # no collitions in this version

    # Redraw
    canvas.create_rectangle(0, 0, pixelWidth, pixelHeight, fill = "white")
    display2DBalls()
    window.update()