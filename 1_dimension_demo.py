import math
from random import random
from time import sleep
from tkinter import *

sleepTime = 0.01  # Delay in seconds between frames

d = 2

width = 1
height = 1
pixelToUnitRatio = 1000
pixelHeight = height * pixelToUnitRatio
pixelWidth = width * pixelToUnitRatio

leftSide = 0
rightSide = pixelWidth

numBalls = 5
balls = []
maxRadius = 0.05
genMaxVel = 0.4

# Create the window.
window = Tk()
window.title("Kinetic Theory of Gases Simulator")
window.resizable(False, False)

# Create the canvas.
canvas = Canvas(window, width = pixelWidth, height = pixelHeight)
canvas.pack()

window.update # ? Is this helpful

class Ball:
    def __init__(self, pos, vel, radius, density):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.diameter = self.radius * 2
        self.density = density
        self.mass = self.density * math.pi * self.radius ** 2
        self.newVelX = None
        # 15 * (1 + 16 + 16 ** 2 + 16 ** 3 + 16 ** 4 + 16 ** 5) = 16777215
        hexBlue = hex(int(density * 255))[2:]
        if len(hexBlue) == 1:
            hexBlue = "0" + hexBlue
        self.color = "#0000" + hexBlue

    def tooClose(a, b, margin, dim=2): #a and b should be vectors of dimension dim
        sum = 0
        for i in range(dim):
            sum += (abs(a[i] - a[b])) ** 2
        return math.sqrt(sum) < margin

    

    def display2DBalls(balls):
        for i in range(numBalls):
            radius = balls[i].radius * pixelToUnitRatio
            posX = balls[i].pos[0] * pixelToUnitRatio
            posY = balls[i].pos[1] * pixelToUnitRatio
            #print(radius, posY, posX)
            canvas.create_oval(posX - radius, posY - radius, posX + radius, posY + radius, fill = balls[i].color)

    # See: https://en.wikipedia.org/wiki/Elastic_collision
    def oneDCollision(mass1, oldVel1, mass2, oldVel2):
        return ((mass1 - mass2) / (mass1 + mass2)) * oldVel1 + mass2 * oldVel2 * 2 / (mass1 + mass2), (2 * mass1 / (mass1 + mass2)) * oldVel1 + ((mass2 - mass1) / (mass1 + mass2)) * oldVel2


# Ball generation
def generateBalls():
    ballsStarted = 0
    while ballsStarted < numBalls:

        potentialPos = []
        for i in range(d):
            potentialPos.append(random())
        potentialRadius = random() * maxRadius
        clear = True

        # * Would accessing the radius only once be better?
        for a in range(0, ballsStarted):
           #this will have to be changed in 3d!`
            if (Ball.tooClose(potentialPos, balls[a].pos, balls[a].radius + potentialRadius) or Ball.tooClose(potentialPos[0], leftSide, balls[a].radius) or Ball.tooClose(potentialX, rightSide, balls[a].radius)):
                clear = False

        if clear:
            balls.append(Ball([potentialX, 0.05], [(2 * (random() - 0.5) * genMaxVel), 0], potentialRadius, random()))
            ballsStarted += 1  # Needs to be at the end for the above math.

generateBalls()

Ball.display2DBalls(balls)

# Animate
for i in range(int(10 / sleepTime)):  # * This should be a 10 second animation.

    # Erase
    canvas.create_rectangle(0, 0, pixelWidth, pixelHeight, fill = "white")

    # Move
    for i in range(numBalls): # TODO: Create better name for width


        if Ball.tooClose(leftSide, balls[i].pos[0], balls[i].radius) or Ball.tooClose(width, balls[i].pos[0], balls[i].radius):  # Doesn't seem to work great.
            balls[i].vel[0] *= -1

        # * Should it move here too?
        # * This is occuring more often than it needs to be, but this may be useful later
        balls[i].pos[0] += balls[i].vel[0] * sleepTime  # Which is pixels moved per tick.

    sleep(sleepTime)

    # Check for and calculate collision.
    for ballA in range(numBalls):

        for ballB in range(ballA + 1, numBalls):
            #print(ballA, ballB)

            if Ball.tooClose(balls[ballA].pos[0], balls[ballB].pos[0], balls[ballA].radius + balls[ballB].radius):

                newVelXA, newVelXB = Ball.oneDCollision(balls[ballA].mass, balls[ballA].vel[0], balls[ballB].mass, balls[ballB].vel[0])

                if balls[ballA].newVelX == None:
                    balls[ballA].newVelX = newVelXA
                else:
                    balls[ballA].newVelX += newVelXA

                if balls[ballB].newVelX == None:
                    balls[ballB].newVelX = newVelXB
                else:
                    balls[ballB].newVelX += newVelXB

    # TODO: I think this whole thing probably needs better boolean zen.
    # Update velocity
    for i in range(numBalls):

        if balls[i].newVelX != None:
            balls[i].vel[0] = balls[i].newVelX

        balls[i].newVelX = None

    # Redraw
    Ball.display2DBalls(balls)
    window.update()