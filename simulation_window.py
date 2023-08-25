import tkinter as tk
import particles as pa

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
        self.balls = []

        # Window
        self.window = window
        window.geometry('700x600')
        window.title('Simulator')
        window.resizable(False, False)
        self.canvas = tk.Canvas(window, width = self.pixelWidth + 20, height = self.pixelHeight + 20)
        self.canvas.create_rectangle(10, 10, self.pixelWidth + 10, self.pixelHeight + 10)
        self.canvas.pack()

        # Create and place balls onto the canvas
        pa.generateBalls(self.canvas, pixelToUnitRatio, self.balls, dimension, self.bounds, numBalls, maxRadius, genMaxVel)

    # Main operation
    def update(self):

        # Move
        for i in range(self.numBalls):

            # If a ball is out of bounds, reverse velocity
            for dim in range(self.dimension):
                # Would it be better to have a variable reference Ball[i]? idk
                if self.balls[i].pos[dim] + self.balls[i].radius > self.bounds[dim][1] or self.balls[i].pos[dim] - self.balls[i].radius < self.bounds[dim][0]:
                    self.balls[i].vel[dim] *= -1

            # Should it move here too?
            # This is occurring more often than it needs to be, but this may be useful later
            self.balls[i].pos[0] += self.balls[i].vel[0] * self.secondsPerTick # Change the ball position by the velocity
            self.balls[i].pos[1] += self.balls[i].vel[1] * self.secondsPerTick # pos[0] = x, pos[1] = y  (units / sec) * (sec / tick) = units / tick

        # Update ball position
        for i in range(self.numBalls):
            posX = self.balls[i].pos[0] * self.pixelToUnitRatio
            posY = self.balls[i].pos[1] * self.pixelToUnitRatio
            # 'moveto' starts at top-left corner as (0, 0)
            self.canvas.moveto(self.balls[i].image, 10 + posX - self.balls[i].radiusPixels, 10 + posY - self.balls[i].radiusPixels)