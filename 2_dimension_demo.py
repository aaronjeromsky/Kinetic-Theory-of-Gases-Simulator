import math
from random import random
from time import sleep
from tkinter import *
from particles import *

#TODO: create a ui so that the user can set some of these variables to whatever they want
#e.g. d, bounds, actual windowsize?, numBalls, maxRadius, genMaxVel, 

#currently geeting a bounding box error; only on the display side of things though.

def update2DBallsDisplay():
        for i in range(numBalls):
            posX = balls[i].pos[0] * pixelToUnitRatio
            posY = balls[i].pos[1] * pixelToUnitRatio
            canvas.moveto(balls[i].image, 10 + posX - balls[i].radiusPixels, 10 + posY - balls[i].radiusPixels) #moveto uses the top left corner of the oval for its coords

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
numBalls = 100
balls = []
maxRadius = 0.5
genMaxVel = 0.5 #maximum velocity that will be generated

# Create the window and canvas
window = Tk()
window.title("Kinetic Theory of Gases Simulator")
window.resizable(False, False)
canvas = Canvas(window, width = pixelWidth + 20, height = pixelHeight + 20)
canvas.create_rectangle(10, 10, pixelWidth + 10, pixelHeight + 10, )
canvas.pack()

#get particles started
window.update # ? Is this helpful
generateBalls(canvas, pixelToUnitRatio, balls, d, bounds, numBalls, maxRadius, genMaxVel)
update2DBallsDisplay() #display initial state

# main loop
def handler():
    #see https://stackoverflow.com/questions/65643645/tkinter-tclerror-invalid-command-name-canvas
    global run
    run = False

window.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:

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

    # Redraw with new positions
    update2DBallsDisplay()
    window.update()

window.destroy()