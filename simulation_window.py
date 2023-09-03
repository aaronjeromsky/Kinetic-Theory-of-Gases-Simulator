import tkinter as tk
import particles as pa
import numpy as np
import variables as va
import itertools as it

class Simulation:

    def __init__(self, window):

        # Internal Variables
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
        # TODO: use variables instead of magic numbers for width and height
        self.canvas = tk.Canvas(window, width=500, height=500)
        self.canvas.configure(bg='#FFFFFF')
        #self.canvas.create_rectangle(0, 0, 500, 500)
        self.canvas.pack()

        # Listen to LMB click on canvas.
        self.canvas.bind('<Button-1>', self.lmb_click)

        # Create and place balls onto the canvas.
        pa.generate_random_balls(self.canvas, self.balls)
        va.avg_vel = self.return_avg_vel()
        va.avg_vel_mag = np.linalg.norm(va.avg_vel)

    def return_avg_vel(self):

        sum_vel = 0

        for ball in self.balls:
            sum_vel += ball.vel

        return sum_vel / va.num_balls

    # Create a new ball where a LMB click was registered.
    def lmb_click(self, event):

        x_coord = event.x
        y_coord = event.y

        pa.place_ball(self, self.canvas, np.array([x_coord, y_coord]), np.array([0, 0]), 0.1, 1, None)

    def update_stats(self):

        sum_vel = 0
        sum_rad = 0
        sum_den = 0

        for ball in self.balls:
            sum_vel += ball.vel
            sum_rad += ball.rad
            sum_den += ball.density

        va.avg_vel = sum_vel / va.num_balls
        va.avg_spd = np.linalg.norm(va.avg_vel)
        va.avg_den = sum_den / va.num_balls
        va.avg_rad = sum_rad / va.num_balls

    # Main operation
    def update(self):

        # ! boundary collisions causes rapid back and forth pulsating
        self.handle_boundary_collisions()
        self.check_for_overlap()
        self.draw_balls()
        # TODO: only update changed values, rad and den won't change often, use a seperate func
        self.update_stats()

    def draw_balls(self):

        for ball in self.balls:

            self.canvas.move(ball.image, ball.vel[0], ball.vel[1])

    # TODO: Performance log to test effectiveness
    # ? Access directly from object or assign data to variable
    def update_ball_velocities(self, ball_1, ball_2):

        pos_1 = ball_1.pos
        pos_2 = ball_2.pos

        disp = np.linalg.norm(pos_1 - pos_2) ** 2

        vel_1 = ball_1.vel
        vel_2 = ball_2.vel

        mass_1 = ball_1.mass
        mass_2 = ball_2.mass
        mass_sum = mass_1 + mass_2

        new_vel_1 = vel_1 - 2 * mass_2 / mass_sum * np.dot(vel_1-vel_2, pos_1 - pos_2) / disp * (pos_1 - pos_2)
        new_vel_2 = vel_2 - 2 * mass_1 / mass_sum * np.dot(vel_2-vel_1, pos_2 - pos_1) / disp * (pos_2 - pos_1)

        ball_1.vel = new_vel_1
        ball_2.vel = new_vel_2

    def check_for_overlap(self):

        pairs = it.combinations(range(va.num_balls), 2)

        for i, j in pairs:

            # ? Is the 'i' and 'j' order correct? What about the one in 'particles.py'
            if pa.overlaps(self.balls[i].pos, self.balls[i].rad, self.balls[j].pos, self.balls[j].rad):

                self.update_ball_velocities(self.balls[i], self.balls[j])

    def handle_boundary_collisions(self):

        for ball in self.balls:

            if ball.pos[0] - ball.rad < 0:
                ball.pos[0] = ball.rad
                ball.vel[0] = -ball.vel[0]

            if ball.pos[0] + ball.rad > 1:
                ball.pos[0] = 1-ball.rad
                ball.vel[0] = -ball.vel[0]

            if ball.pos[1] - ball.rad < 0:
                ball.pos[1] = ball.rad
                ball.vel[1] = -ball.vel[1]

            if ball.pos[1] + ball.rad > 1:
                ball.pos[1] = 1-ball.rad
                ball.vel[1] = -ball.vel[1]