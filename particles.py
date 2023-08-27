import random as ra
import math as ma
import numpy as np

class Ball:

    def __init__(self, canvas, pixelToUnitRatio, pos, vel, radius, density):

        self.pos = pos
        self.vel = vel # pos and vel are vectors with dimension d
        self.radius = radius
        self.diameter = self.radius * 2 #does using radius vs self.radius matter?
        self.density = density
        self.mass = self.density * ma.pi * (self.radius ** 2)

        # Position and velocity are vectors with dimension d.
        self.pos = pos
        self.vel = vel
        self.newVelX = None #TODO this system isn't very good
        # 15 * (1 + 16 + 16 ** 2 + 16 ** 3 + 16 ** 4 + 16 ** 5) = 16777215
        hexBlue = hex(int(density * 255))[2:]
        if len(hexBlue) == 1:
            hexBlue = "0" + hexBlue
        self.color = "#0000" + hexBlue

        self.canvas = canvas
        #the following only works for 2d
        self.radiusPixels = self.radius * pixelToUnitRatio
        self.diameterPixels = self.radiusPixels * 2 # ? Is there be a way to deallocate 'self.diameterPixels'? Is that done automatically?

        self.canvas = canvas
        self.image = self.canvas.create_oval(0, 0, self.diameterPixels, self.diameterPixels, fill = self.color)
        #self.numText = self.canvas.create_text(0, 0, text=str(number))

def vel1AfterCollision(ball1, ball2):
    # See: https://en.wikipedia.org/wiki/Elastic_collision
    # and https://stackoverflow.com/questions/9171158/how-do-you-get-the-magnitude-of-a-vector-in-numpy
    displacementBtwnCenters = ball1.pos - ball2.pos #shorter var name would be nice
    return ball1.vel - (2 * ball2.mass * np.dot(ball1.vel - ball2.vel, displacementBtwnCenters) * displacementBtwnCenters) / ((ball1.mass + ball2.mass) * (np.linalg.norm(displacementBtwnCenters) ** 2))

def tooClose(pos1, pos2, radius1, radius2, dimension = 2): # a and b should be vectors of dimension  # ? What order should the arguments be in?
        # the arguments aren't the balls themselves, so that generate Balls can use this, maybe change that later?
        # i put this outside of the ball class because i want to it to be able to be used in generateBalls before actually generating ball objects
        return np.linalg.norm(pos1 - pos2) <= radius1 + radius2  #how much margin do we need for things not to phase into each other?

def generateBalls(canvas, pixelToUnitRatio, balls, d, bounds, numBalls, maxRadius, genMaxVel):

    minRadius = maxRadius * 0.2

    ballsStarted = 0

    while ballsStarted < numBalls:

        # generate values for a potential new ball
        potentialPos = np.zeros(d)

        for i in range(d):
            potentialPos[i] = ra.random()

        potentialRadius = minRadius + ra.random() * (maxRadius - minRadius)
        clear = True #I considered using continue, but i don't know how that would work with nested loops

        #check that the ball is in bounds
        for dim in range(d):  #integrate this with the boundary checking during animation?

            if potentialPos[dim] + potentialRadius > bounds[dim][1] or potentialPos[dim] - potentialRadius < bounds[dim][0]: #would it be better to have a variable reference Ball[i]? idk
                clear = False #what do you think about using continue ?
            # * Would accessing the radius only once be better?

        #check that the ball isn't touching an already placed ball
        for otherBallIndex in range(0, ballsStarted):

            if tooClose(potentialPos, balls[otherBallIndex].pos, potentialRadius, balls[otherBallIndex].radius):
                clear = False
                break

        #create the new ball if conditions are right
        if clear:

            #generate a random ndimensional velocity
            newVel = np.zeros(d) # creates a d long array full of zeros
            for v in range(d):
                newVel[v] = 2 * (ra.random() - 0.5) * genMaxVel
                #newVel[v] = genMaxVel
            #density 0.2 + ra.random() * 0.8
            balls.append(Ball(canvas, pixelToUnitRatio, potentialPos, newVel, potentialRadius, 1))
            ballsStarted += 1  # Needs to be at the end for the above math.