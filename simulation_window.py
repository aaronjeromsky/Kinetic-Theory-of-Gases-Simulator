import tkinter as tk
import particles as pa
import numpy as np

class Simulation:

    # Is there a less repetitive way to use 'self'?
    def __init__(self, window, seconds_per_tick, dimension, pixel_to_unit_ratio, number_of_balls, maximum_radius, maximum_velocity):

        # Parameter Variables
        self.seconds_per_tick = seconds_per_tick
        self.dimension = dimension
        self.pixel_to_unit_ratio = pixel_to_unit_ratio
        self.number_of_balls = number_of_balls
        self.maximum_radius = maximum_radius
        self.maximum_velocity = maximum_velocity

        # Internal Variables

        # It can be a rectangle, rectangular prism, etc.
        self.bounds = []
        self.sizes = []

        for i in range(dimension):

            # This makes a 1 by 1 box, should be something the user can change?
            # For now it's [[0, 1], [0, 1]]
            self.bounds.append([0, 1])
            self.sizes.append(abs(self.bounds[i][1] - self.bounds[i][0]))

        self.width = self.sizes[0]
        self.height = self.sizes[1]

        self.pixel_width = self.width * pixel_to_unit_ratio
        self.pixel_height = self.height * pixel_to_unit_ratio

        self.left_side = 0
        self.right_side = self.pixel_width
        self.balls = []  # this is the main list that all the ball objects are stored in!

        # Window
        self.window = window

        ww = 600
        wh = 600
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()

        x = (sw / 2) - (ww / 2) + 250
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Simulator')
        window.resizable(False, False)
        self.canvas = tk.Canvas(window, width = self.pixel_width, height = self.pixel_height)
        # 2, 2 to make canvas border visible.
        self.canvas.create_rectangle(2, 2, self.pixel_width, self.pixel_height)
        self.canvas.pack()

        # Listen to mouse-click events on canvas.
        self.canvas.bind('<Button-1>', self.left_mouse_click)

        # Create and place balls onto the canvas.
        pa.generateBalls(self.canvas, pixel_to_unit_ratio, self.balls, dimension, self.bounds, number_of_balls, maximum_radius, maximum_velocity)

    # Create a new ball where a LMB click was registered.
    def left_mouse_click(self, event):

        x_coord = event.x
        y_coord = event.y

        pa.place_ball(self, self.canvas, 500, [x_coord / self.pixel_to_unit_ratio, y_coord / self.pixel_to_unit_ratio], [0.1, 0.1], 0.1, 0.5)
        self.number_of_balls += 1

    # Main operation
    def update(self):

        # Each ball moves due to its velocity.
        for i in range(self.number_of_balls):

            # If a ball is out of bounds, reverse velocity
            # Only works if the container is rectangular.
            for dim in range(self.dimension):

                # ? Would it be better to have a variable reference Ball[i]?
                # Collision with the walls
                if self.balls[i].position[dim] + self.balls[i].radius > self.bounds[dim][1] or self.balls[i].position[dim] - self.balls[i].radius < self.bounds[dim][0]:
                    self.balls[i].velocity[dim] *= -1

            # Test and effect collisions
            for outer in range(self.number_of_balls): # These two loops look at every possible pair of balls

                for inner in range(outer + 1, self.number_of_balls):  # + 1 so that it won't compare a ball against itself

                    #print(outer, inner)
                    if pa.tooClose(self.balls[inner].position, self.balls[outer].position, self.balls[inner].radius, self.balls[outer].radius, 2):

                        # Remember to swap around!
                        #print(outer, inner)
                        tempVel = pa.vel1AfterCollision(self.balls[inner], self.balls[outer])
                        self.balls[outer].velocity = pa.vel1AfterCollision(self.balls[outer], self.balls[inner])
                        self.balls[inner].velocity = tempVel
                        #print(self.balls[inner].velocity, self.balls[outer].velocity)
                        #print(outer, inner)

            # TODO: Optimize code
            # Changes the positon based on velocity per unit time.
            self.balls[i].position[0] += self.balls[i].velocity[0] * self.seconds_per_tick # Change the ball position by the velocity
            self.balls[i].position[1] += self.balls[i].velocity[1] * self.seconds_per_tick # position[0] = x, position[1] = y  (units / sec) * (sec / tick) = units / tick

        # Display the new ball positions
        for i in range(self.number_of_balls):

            positionX = self.balls[i].position[0] * self.pixel_to_unit_ratio
            positionY = self.balls[i].position[1] * self.pixel_to_unit_ratio

            # 'moveto' starts at top-left corner as (0, 0)
            self.canvas.moveto(self.balls[i].image, positionX - self.balls[i].pixel_radius, positionY - self.balls[i].pixel_radius)