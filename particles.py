import random as ra
import math as ma
import numpy as np
import variables as va

class Ball:

    # TODO: update default values
    def __init__(self, canvas, pos=np.array([250, 250]), vel=np.array([0, 0]), rad=50, density=1, color=None):

        # Parameters
        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.density = density

        # Generates a monochrome color (represneting density) when no color is provided
        if (color is None):
            color_value = lambda : int(255 - density * 255)
            self.color = '#{:02x}{:02x}{:02x}'.format(color_value(), color_value(), color_value())
        else:
            self.color = color

        self.diameter = rad * 2
        self.mass = density * ma.pi * (rad ** 2)

        self.canvas = canvas

        # ! The oval image may not match the internal calculations
        self.image = self.canvas.create_oval(pos[0] - rad, pos[1] - rad, pos[0] + rad, pos[1] + rad, fill = self.color, width = 0)

        va.num_balls += 1

# Returns true if balls are overlapping, false otherwise.
def overlaps(pos_1, rad_1, pos_2, rad_2):

    return np.hypot(*(pos_1 - pos_2)) < rad_1 + rad_2

# ? Should this use 'self.balls' or just the parameter 'balls'
def place_ball(self, canvas, pos, vel, radius, density, color=None):

    self.balls.append(Ball(canvas, pos, vel, radius, density, color))

def generate_random_balls(canvas, balls):

    while va.num_balls < va.balls_to_create:

        # Initial random values for the ball
        # TODO: compensate for ball radius when setting position to avoid overlapping walls
        pos = np.array([ra.uniform(0, 500), ra.uniform(0, 500)])
        rad = 15

        # Check if the ball overlaps an existing one
        for ball in balls:
            if (overlaps(ball.pos, ball.rad, pos, rad)):
                break
        else:
            # remaning random values for the ball
            vel = np.array([ra.uniform(0, 5), ra.uniform(0, 5)])
            density = ra.uniform(0, 1)

            # Create the ball
            new_ball = Ball(canvas, pos, vel, rad, density)

            # Append the ball to the ball list
            balls.append(new_ball)