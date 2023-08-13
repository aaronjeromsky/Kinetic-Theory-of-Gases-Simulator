from random import random
import math

class Ball:
    def __init__(self, pos, vel, radius, density):
        self.pos = pos
        self.vel = vel # pos and vel are vectors with dimension d
        self.radius = radius
        self.density = density
        self.mass = self.density * math.pi * self.radius ** 2
        self.newVelX = None #TODO this system isn't very good
        # 15 * (1 + 16 + 16 ** 2 + 16 ** 3 + 16 ** 4 + 16 ** 5) = 16777215
        hexBlue = hex(int(density * 255))[2:]
        if len(hexBlue) == 1:
            hexBlue = "0" + hexBlue
        self.color = "#0000" + hexBlue

    def oneDCollision(mass1, oldVel1, mass2, oldVel2):
        # See: https://en.wikipedia.org/wiki/Elastic_collision
        return ((mass1 - mass2) / (mass1 + mass2)) * oldVel1 + mass2 * oldVel2 * 2 / (mass1 + mass2), (2 * mass1 / (mass1 + mass2)) * oldVel1 + ((mass2 - mass1) / (mass1 + mass2)) * oldVel2
    
def tooClose(pos1, pos2, radius1, radius2, dim=2): #a and b should be vectors of dimension dim  #what order should the args be?
        # i put this outside of the ball class because i want to it to be able to be used in generateBalls before actually generating ball objects
        sum = 0
        for i in range(dim):
            sum += (abs(pos1[i] - pos2[i])) ** 2
        return math.sqrt(sum) <= radius1 + radius2  #how much margin do we need for things not to phase into each other?

def generateBalls(balls, d, bounds, numBalls, maxRadius, genMaxVel):
    ballsStarted = 0
    while ballsStarted < numBalls:
        #generate values for a potential new ball    
        potentialPos = []
        for i in range(d):
            potentialPos.append(random())
        potentialRadius = random() * maxRadius
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
            balls.append(Ball(potentialPos, [(2 * (random() - 0.5) * genMaxVel), (2 * (random() - 0.5) * genMaxVel)], potentialRadius, random()))
            ballsStarted += 1  # Needs to be at the end for the above math.