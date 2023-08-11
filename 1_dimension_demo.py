import tkinter
import math
from random import random
from time import sleep

class Ball:
    def __init__(self, posX, posY, velX, velY, radius, density):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.radius = radius
        # self.diameter = self.radius * 2  # do we need self.? also do we need diameter?
        self.density = density
        self.mass = self.density * math.pi * self.radius**2
        self.newVelX = None
        # 15 * ( 1 + 16 + 16 ** 2 + 16 **3 + 16 ** 4 + 16 ** 5) = 16777215
        hexBlue = hex(int(density * 255))[2:]
        if len(hexBlue) == 1:
            hexBlue = "0" + hexBlue
        self.color = "#0000" + hexBlue

def tooClose(a, b, margin):
    return abs(a - b) < margin

def displayBalls(balls):
    for i in range(numBalls):
        radius = balls[i].radius * pixelToUnitRatio
        posX = balls[i].posX * pixelToUnitRatio
        posY = balls[i].posY * pixelToUnitRatio
        # print(radius, posY, posX)
        canvas.create_oval(posX - radius, posY - radius, posX + radius, posY + radius, fill = balls[i].color)

# See: https://en.wikipedia.org/wiki/Elastic_collision
def oneDCollision(mass1, oldVel1, mass2, oldVel2):
    # TODO: Provide formating that is easier to read.
    return ((mass1 - mass2) / (mass1 + mass2)) * oldVel1 + mass2 * oldVel2 * 2 / (mass1 + mass2), (2 * mass1 / (mass1 + mass2)) * oldVel1 + ((mass2 - mass1) / (mass1 + mass2)) * oldVel2

sleepTime = 0.01  # Seconds

width = 1
height = 0.1
pixelToUnitRatio = 1000
pixelHeight = height * pixelToUnitRatio
pixelWidth = width * pixelToUnitRatio

leftSide = 0
rightSide = pixelWidth

numBalls = 5
balls = []
maxRadius = 0.05
genMaxVel = 0.4

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=pixelWidth, height=pixelHeight)
canvas.pack()

# Ball generation
ballsStarted = 0
while ballsStarted < numBalls:

    potentialX = random()
    potentialRadius = random() * maxRadius
    clear = True

    # * Would accessing the radius only once be better?
    for a in range(0, ballsStarted):

        if (tooClose(potentialX, balls[a].posX, balls[a].radius + potentialRadius) or tooClose(potentialX, leftSide, balls[a].radius) or tooClose(potentialX, rightSide, balls[a].radius)):
            clear = False

    if clear:
        balls.append(Ball(potentialX, 0.05, (2 * (random() - 0.5) * genMaxVel), 0, potentialRadius, random()))
        ballsStarted += 1  # Needs to be at the end for the above math.

displayBalls(balls)

# Animate
for i in range(int(10 / sleepTime)):  # * This should be a 10 second animation.

    # Erase
    canvas.create_rectangle(0, 0, pixelWidth, pixelHeight, fill = "white")

    # Move
    for i in range(numBalls):  # TODO: Create better name for width

        if tooClose(leftSide, balls[i].posX, balls[i].radius) or tooClose(width, balls[i].posX, balls[i].radius):  # Doesn't seem to work great.
            balls[i].velX *= -1

        # * Should it move here too?
        # * This is occuring more often than it needs to be, but this may be useful later
        balls[i].posX += balls[i].velX * sleepTime  # Which is pixels moved per tick.

    sleep(sleepTime)

    # Check for and calculate collision.
    for ballA in range(numBalls):

        for ballB in range(ballA + 1, numBalls):
            print(ballA, ballB)

            if tooClose(balls[ballA].posX, balls[ballB].posX, balls[ballA].radius + balls[ballB].radius):

                newVelXA, newVelXB = oneDCollision(balls[ballA].mass, balls[ballA].velX, balls[ballB].mass, balls[ballB].velX)

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
            balls[i].velX = balls[i].newVelX

        balls[i].newVelX = None

    # Redraw
    displayBalls(balls)
    window.update()

window.mainloop()