import random as ra
import math as ma
import numpy as np

# Multiplication is faster than to exponentiation (except ** 2 and massive values), use this to optimize code.
# See: https://stackoverflow.com/questions/18453771/why-is-x3-slower-than-xxx/18453999#18453999

class Ball:

    def __init__(self, canvas, pixel_to_unit_ratio, position, velocity, radius, density):

        # Parameters

        # Position and velocity are vectors.
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.diameter = radius * 2
        self.density = density
        self.mass = density * ma.pi * (radius ** 2)

        # Ball color
        blue_hex = hex(int(density * 255))[2:]

        if len(blue_hex) == 1:
            blue_hex = "0" + blue_hex

        self.color = "#0000" + blue_hex

        # The following couple lines only work in a 2D environment.
        self.pixel_radius = self.radius * pixel_to_unit_ratio
        self.pixel_diameter = self.pixel_radius * 2

        self.canvas = canvas
        self.image = self.canvas.create_oval(0, 0, self.pixel_diameter, self.pixel_diameter, fill = self.color, width = 0)
        #self.numText = self.canvas.create_text(0, 0, text=str(number))

def vel1AfterCollision(ball1, ball2):

    # See: https://en.wikipedia.org/wiki/Elastic_collision
    # and https://stackoverflow.com/questions/9171158/how-do-you-get-the-magnitude-of-a-vector-in-numpy
    displacementBtwnCenters = ball1.position - ball2.position #shorter var name would be nice

    return ball1.velocity - (2 * ball2.mass * np.dot(ball1.velocity - ball2.velocity, displacementBtwnCenters) * displacementBtwnCenters) / ((ball1.mass + ball2.mass) * (np.linalg.norm(displacementBtwnCenters) ** 2))

def tooClose(position1, position2, radius1, radius2, dimension): # a and b should be vectors of dimension  # ? What order should the arguments be in?

        # the arguments aren't the balls themselves, so that generate Balls can use this, maybe change that later?
        # i put this outside of the ball class because i want to it to be able to be used in generateBalls before actually generating ball objects
        return np.linalg.norm(position1 - position2) <= radius1 + radius2  #how much margin do we need for things not to phase into each other?

def place_ball(self, canvas, pixel_to_unit_ratio, position, velocity, radius, density):

    self.balls.append(Ball(canvas, pixel_to_unit_ratio, position, velocity, radius, density))

def generateBalls(canvas, pixel_to_unit_ratio, balls, dimension, bounds, number_of_balls, maximum_radius, maximum_velocity):

    minimum_radius = maximum_radius * 0.2
    balls_started = 0

    while balls_started < number_of_balls:

        # generate values for a potential new ball
        potential_position = np.zeros(dimension)

        for i in range(dimension):
            potential_position[i] = ra.random()

        potential_radius = minimum_radius + ra.random() * (maximum_radius - minimum_radius)
        clear = True #I considered using continue, but i don't know how that would work with nested loops

        #check that the ball is in bounds
        for dimensions in range(dimension):  #integrate this with the boundary checking during animation?

            if potential_position[dimensions] + potential_radius > bounds[dimensions][1] or potential_position[dimensions] - potential_radius < bounds[dimensions][0]: #would it be better to have a variable reference Ball[i]? idk
                clear = False #what do you think about using continue ?
            # * Would accessing the radius only once be better?

        #check that the ball isn't touching an already placed ball
        for other_ball_index in range(0, balls_started):

            if tooClose(potential_position, balls[other_ball_index].position, potential_radius, balls[other_ball_index].radius, 2):
                clear = False
                break

        #create the new ball if conditions are right
        if clear:

            #generate a random n-dimensional velocity
            new_velocity = np.zeros(dimension) # creates a dimension long array full of zeros

            for v in range(dimension):
                new_velocity[v] = 2 * (ra.random() - 0.5) * maximum_velocity
                #new_velocity[v] = maximum_velocity

            #density 0.2 + ra.random() * 0.8
            balls.append(Ball(canvas, pixel_to_unit_ratio, potential_position, new_velocity, potential_radius, 1))
            balls_started += 1  # Needs to be at the end for the above math.