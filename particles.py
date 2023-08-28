import random as ra
import math as ma
import numpy as np
import variables as va

class Ball:

    # TODO: make color an optional argument.
    def __init__(self, canvas, pos, vel, radius, density, color):

        # Parameters

        # pos and vel are vectors.
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.diameter = radius * 2
        self.density = density
        self.mass = density * ma.pi * (radius ** 2)

        # Color
        if (color is None or color == ''):
            color_value = lambda : ra.randint(0,255)
            self.color = '#{:02x}{:02x}{:02x}'.format(color_value(), color_value(), color_value())
        else:
            self.color = color

        # The following couple lines only work in a 2D environment.
        self.pixel_radius = self.radius * va.pixel_to_unit_ratio
        self.pixel_diameter = self.pixel_radius * 2

        self.canvas = canvas
        self.image = self.canvas.create_oval(0, 0, self.pixel_diameter, self.pixel_diameter, fill = self.color, width = 0)
        #self.numText = self.canvas.create_text(0, 0, text=str(number))


    

# TODO: 'a' and 'b' should be vectors of 'dimension'
# ? What order should the arguments be in?
def tooClose(pos1, pos2, radius1, radius2):

        # The arguments aren't the balls themselves, so that generate Balls can use this, maybe change that later?
        # I put this outside of the ball class because i want to it to be able to be used in generateBalls before actually generating ball objects.
        # How much margin do we need for things not to phase into each other?
        return np.linalg.norm(pos1 - pos2) <= radius1 + radius2

def place_ball(self, canvas, pos, vel, radius, density, color):

    self.balls.append(Ball(canvas, pos, vel, radius, density, color))

def generateBalls(canvas, balls, bounds):

    minimum_radius = va.maximum_radius * 0.2
    balls_started = 0

    while balls_started < va.number_of_balls:

        # generate values for a potential new ball
        potential_pos = np.zeros(va.dimension)

        for i in range(va.dimension):
            potential_pos[i] = ra.random()

        potential_radius = minimum_radius + ra.random() * (va.maximum_radius - minimum_radius)

        # TODO: see if using 'continue' is a better approach than using a boolean.
        clear = True

        # Check if the ball is in bounds
        # TODO: integrate this with the boundary checking during animation.
        for dimensions in range(va.dimension):

            if potential_pos[dimensions] + potential_radius > bounds[dimensions][1] or potential_pos[dimensions] - potential_radius < bounds[dimensions][0]:
                clear = False

        #check that the ball isn't touching an already placed ball
        for other_ball_index in range(0, balls_started):

            if tooClose(potential_pos, balls[other_ball_index].pos, potential_radius, balls[other_ball_index].radius):
                clear = False
                break

        #create the new ball if conditions are right
        if clear:

            #generate a random n-dimensional vel
            new_vel = np.zeros(va.dimension) # creates a dimension long array full of zeros

            for v in range(va.dimension):
                new_vel[v] = 2 * (ra.random() - 0.5) * va.max_gen_units_per_tick
                #new_vel[v] = va.maximum_vel

            #density 0.2 + ra.random() * 0.8
            balls.append(Ball(canvas, potential_pos, new_vel, potential_radius, 1, None))
            balls_started += 1  # Needs to be at the end for the above math.