import random as ra
import math as ma
import numpy as np
import variables as va

class Ball:

    # TODO: update default values
    def __init__(self, canvas, pos=np.array([250, 250]), vel=np.array([0, 0]), rad=0.1, density=1, color=None):

        # Parameters
        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.density = density

        # Generates a monochrome color (represneting density) when no color is provided
        if (color is None):
            color_value = lambda : int(density * 255)
            self.color = '#{:02x}{:02x}{:02x}'.format(color_value(), color_value(), color_value())
        else:
            self.color = color

        self.diameter = rad * 2
        self.mass = density * ma.pi * (rad ** 2)

        self.canvas = canvas

        # ! The oval image may not match the internal calculations
        self.image = self.canvas.create_oval(pos[0], pos[1], pos[0] + self.diameter, pos[1] + self.diameter, fill = self.color, width = 0)

        va.num_balls += 1

# Returns true if balls aren't overlapping, false otherwise.
def overlaps(pos_1, rad_1, pos_2, rad_2):

    return np.hypot(*(pos_1 - pos_2)) < rad_1 + rad_2

# ? Should this use 'self.balls' or just the parameter 'balls'
def place_ball(self, canvas, pos, vel, radius, density, color):

    self.balls.append(Ball(canvas, pos, vel, radius, density, color))

def generate_random_balls(canvas, balls):

    while va.num_balls < va.balls_to_create:

        # Initial random values for the ball
        pos = np.array([ra.uniform(0, 500), ra.uniform(0, 500)])
        rad = ra.uniform(0, 50)

        # Check if the ball overlaps an existing one
        for ball in balls:
            if (overlaps(ball.pos, ball.rad, pos, rad)):
                break
        else:
            # remaning random values for the ball
            vel = np.array([ra.uniform(0, 1), ra.uniform(0, 1)])
            density = ra.uniform(0, 1)
            color = None

            # Create the ball
            new_ball = Ball(canvas, pos, vel, rad, density, color)

            # Append the ball to the ball list
            balls.append(new_ball)