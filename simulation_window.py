import tkinter as tk
import particles as pa
import numpy as np # for testing, can remove later

class Simulation:

    # Double-check that 'self' is used correctly
    def __init__(self, window, secondsPerTick, dimension, pixelToUnitRatio, numBalls, maxRadius, genMaxVel):

        # Parameter Variables
        self.secondsPerTick = secondsPerTick
        self.dimension = dimension
        self.pixelToUnitRatio = pixelToUnitRatio
        self.numBalls = numBalls
        self.maxRadius = maxRadius
        self.genMaxVel = genMaxVel

        # Internal Variables

        # It will be a rectangle, rectangular prism, etc
        self.bounds = []
        self.sizes = []

        for i in range(self.dimension):

            # This makes a 1 by 1 box, but this should be something the user can change?
            # For now it's [[0, 1], [0, 1]]
            self.bounds.append([0, 1])
            self.sizes.append(abs(self.bounds[i][1] - self.bounds[i][0]))

        self.width = self.sizes[0]
        self.height = self.sizes[1]

        self.pixelWidth = self.width * self.pixelToUnitRatio
        self.pixelHeight = self.height * self.pixelToUnitRatio

        self.leftSide = 0
        self.rightSide = self.pixelWidth
        self.balls = []  # this is the main list that all the ball objects are stored in!

        # Window
        self.window = window
        window.geometry('700x600')
        window.title('Simulator')
        window.resizable(False, False)
        self.canvas = tk.Canvas(window, width = self.pixelWidth, height = self.pixelHeight)
        self.canvas.create_rectangle(2, 2, self.pixelWidth, self.pixelHeight)
        self.canvas.pack()

        # Create and place balls onto the canvas
        pa.generateBalls(self.canvas, pixelToUnitRatio, self.balls, dimension, self.bounds, numBalls, maxRadius, genMaxVel)

    # Main operation
    def update(self):

        # each ball moves due to its velocity
        for i in range(self.numBalls):

            # If a ball is out of bounds, reverse velocity    # only works if the container is rectangular
            for dim in range(self.dimension):
                # ? Would it be better to have a variable reference Ball[i]? idk
                # Collision with the walls
                if self.balls[i].pos[dim] + self.balls[i].radius > self.bounds[dim][1] or self.balls[i].pos[dim] - self.balls[i].radius < self.bounds[dim][0]:
                    self.balls[i].vel[dim] *= -1

            # #test and effect collisions
            for outer in range(self.numBalls): # these two loops look at every possible pair of balls
                for inner in range(outer + 1, self.numBalls):  # + 1 so that it won't compare a ball against itself
                    #print(outer, inner)
                    if pa.tooClose(self.balls[inner].pos, self.balls[outer].pos, self.balls[inner].radius, self.balls[outer].radius):
                        #remember to swap around!
                        #print(outer, inner)
                        tempVel = pa.vel1AfterCollision(self.balls[inner], self.balls[outer])
                        self.balls[outer].vel = pa.vel1AfterCollision(self.balls[outer], self.balls[inner])
                        self.balls[inner].vel = tempVel
                        #print(self.balls[inner].vel, self.balls[outer].vel)
                        #print(outer, inner)

            # ? Should it move here too?
            # can this be optimized?
            # Changes the positon based on velocity per unit time.
            self.balls[i].pos[0] += self.balls[i].vel[0] * self.secondsPerTick # Change the ball position by the velocity
            self.balls[i].pos[1] += self.balls[i].vel[1] * self.secondsPerTick # pos[0] = x, pos[1] = y  (units / sec) * (sec / tick) = units / tick

        # Display the new ball positions
        for i in range(self.numBalls):
            posX = self.balls[i].pos[0] * self.pixelToUnitRatio
            posY = self.balls[i].pos[1] * self.pixelToUnitRatio
            # 'moveto' starts at top-left corner as (0, 0)
            self.canvas.moveto(self.balls[i].image, posX - self.balls[i].radiusPixels, posY - self.balls[i].radiusPixels)