import random as ra
import math as ma
import numpy as np
import variables as va

class Ball:

    def __init__(self, canvas, pos=np.array([0, 0]), vel=np.array([0, 0]), radius=0.1, density=1, color=None):

        # Parameters
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.diameter = radius * 2
        self.density = density
        self.mass = density * ma.pi * (radius ** 2)

        # Generate a random color if none is provided
        if (color is None):
            color_value = lambda : ra.randint(0,255)
            self.color = '#{:02x}{:02x}{:02x}'.format(color_value(), color_value(), color_value())
        else:
            self.color = color

        # The following couple lines only work in a 2D environment.
        self.pixel_radius = self.radius * va.pixel_to_unit_ratio
        self.pixel_diameter = self.pixel_radius * 2

        self.canvas = canvas
        self.image = self.canvas.create_oval(0, 0, self.pixel_diameter, self.pixel_diameter, fill = self.color, width = 0)

    # Returns true is balls aren't overlapping, false otherwise.
    def overlaps(self, other):

        return np.hypot(*(self.pos - other.pos)) < self.radius + other.radius

def place_ball(self, canvas, pos, vel, radius, density, color):

    self.balls.append(Ball(canvas, pos, vel, radius, density, color))

def generate_random_balls(canvas, balls):

    num_balls_created = 0

    while num_balls_created < va.number_of_balls:

        # Random values for a ball
        # TODO: find and use optimal min and max values.
        pos = np.array([ra.uniform(0, 1), ra.uniform(0, 1)])
        vel = np.array([ra.uniform(0, 0.0001), ra.uniform(0, 0.0001)])
        radius = ra.uniform(0, 0.1)
        density = ra.uniform(0, 1)
        color = None

        new_ball = Ball(canvas, pos, vel, radius, density, color)

        for old_ball in balls:
            if (old_ball.overlaps(new_ball)):
                break

        balls.append(new_ball)
        num_balls_created += 1