import tkinter as tk
import particles as pa
import numpy as np
import variables as va

class Simulation:

    def __init__(self, window):

        # Internal Variables

        # It can be a rectangle, rectangular prism, etc.
        self.bounds = []
        self.sizes = []

        for i in range(va.dimension):

            # This makes a 1 by 1 box, should be something the user can change?
            # For now it's [[0, 1], [0, 1]]
            self.bounds.append([0, 1])
            self.sizes.append(abs(self.bounds[i][1] - self.bounds[i][0]))

        self.width = self.sizes[0]
        self.height = self.sizes[1]

        self.pixel_width = self.width * va.pixel_to_unit_ratio
        self.pixel_height = self.height * va.pixel_to_unit_ratio

        self.left_side = 0
        self.right_side = self.pixel_width
        self.balls = []

        # Window
        self.window = window

        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 600
        wh = 600

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
        pa.generateBalls(self.canvas, self.balls, self.bounds)
        va.avg_vel = self.return_avg_vel()
        va.avg_vel_mag = np.linalg.norm(va.avg_vel)

    def return_avg_vel(self):
        #why does it need self as an arg?
        total_vel = 0
        for ball in self.balls:
            total_vel += ball.vel

        return total_vel / va.number_of_balls

    # Create a new ball where a LMB click was registered.
    def left_mouse_click(self, event):

        x_coordinate = event.x
        y_coordinate = event.y

        # Adapt to numpy
        pa.place_ball(self, self.canvas, np.array([x_coordinate / va.pixel_to_unit_ratio, y_coordinate / va.pixel_to_unit_ratio]), np.array([va.max_gen_units_per_tick, va.max_gen_units_per_tick]), 0.1, 1, None)
        va.number_of_balls += 1

    # Main operation
    def update(self):

        # Each ball moves due to its vel.
        for i in range(va.number_of_balls):
            no_wall_bounce = True
             

                

            # Test and effect collisions
            # TODO: calculate collision wihtout checking every ball at once.
            for outer in range(va.number_of_balls):

                for inner in range(outer + 1, va.number_of_balls):  # + 1 so that it won't compare a ball against itself

                    #find displacement and magnitude btwn outer and inner balls
                    disp_o_i = self.balls[outer].pos - self.balls[inner].pos
                    disp_i_o = -1 * disp_o_i
                    mag_o_i = np.linalg.norm(disp_o_i)

                    #print(outer, inner)
                    if mag_o_i <= self.balls[inner].radius + self.balls[outer].radius:

                        # Remember to swap around!
                        #print(outer, inner)

                        # See: https://en.wikipedia.org/wiki/Elastic_collision
                        # and https://stackoverflow.com/questions/9171158/how-do-you-get-the-magnitude-of-a-vector-in-numpy

                        temporary_vel = self.balls[inner].vel - (2 * self.balls[outer].mass * np.dot(self.balls[inner].vel - self.balls[outer].vel, disp_o_i) * disp_o_i) / ((self.balls[inner].mass + self.balls[outer].mass) * (mag_o_i ** 2))
                        self.balls[outer].vel = self.balls[outer].vel - (2 * self.balls[inner].mass * np.dot(self.balls[outer].vel - self.balls[inner].vel, disp_i_o) * disp_i_o) / ((self.balls[outer].mass + self.balls[inner].mass) * (mag_o_i ** 2))
                        self.balls[inner].vel = temporary_vel
                        #print(self.balls[inner].vel, self.balls[outer].vel)
                        #print(outer, inner)

                #balls change pos due to vel
                self.balls[i].pos += self.balls[i].vel
                
                #If a ball is out of bounds, reverse vel
                # Only works if the container is rectangular.
                for dim in range(va.dimension):
                    # ? Would it be better to have a variable reference Ball[i]?
                    # Collision with the walls
                    if self.balls[i].pos[dim] + self.balls[i].radius > self.bounds[dim][1]:
                        
                        # can the first two blocks be integrated with out losing efficiency?
                        time_before = (self.bounds[dim][1] - self.balls[i].radius - self.balls[i].pos[dim]) / self.balls[i].vel[dim]
                        # time_after + time_before = 1 tick
                        time_after = 1 - time_before
                        old_vel = self.balls[i].vel

                        #reset the ball to where is was before clipping
                        self.balls[i].pos -= self.balls[i].vel

                        #set the ball object to store what the new vel will be, while keeping the old vel in a temp var
                        self.balls[i].vel[dim] = -1 * self.balls[i].vel[dim]
                        self.balls[i].pos = self.balls[i].pos + old_vel * time_before + self.balls[i].vel * time_after
                        self.balls[i].pos[dim] -= va.bouncing_fudge_factor
                    elif self.balls[i].pos[dim] - self.balls[i].radius < self.bounds[dim][0]:
                        
                        time_before = (self.bounds[dim][0] + self.balls[i].radius - self.balls[i].pos[dim]) / self.balls[i].vel[dim]
                        # time_after + time_before = 1 tick
                        time_after = 1 - time_before
                        old_vel = self.balls[i].vel

                        #reset the ball to where is was before clipping
                        self.balls[i].pos -= self.balls[i].vel

                        #set the ball object to store what the new vel will be, while keeping the old vel in a temp var
                        self.balls[i].vel[dim] = -1 * self.balls[i].vel[dim]
                        self.balls[i].pos = self.balls[i].pos + old_vel * time_before + self.balls[i].vel * time_after
                        self.balls[i].pos[dim] += va.bouncing_fudge_factor

                
                    

            
        # Display the new ball poss
        for i in range(va.number_of_balls):
            #print(self.balls[i].vel * va.pixel_to_unit_ratio)
            x_pos = self.balls[i].pos[0] * va.pixel_to_unit_ratio
            y_pos = self.balls[i].pos[1] * va.pixel_to_unit_ratio

            # 'moveto' starts at top-left corner as (0, 0)
            self.canvas.moveto(self.balls[i].image, x_pos - self.balls[i].pixel_radius, y_pos - self.balls[i].pixel_radius)