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

        x = (sw / 2) - (ww / 2)
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Simulator')
        window.resizable(False, False)
        # TODO: use variables instead of magic numbers for width and height
        self.canvas = tk.Canvas(window, width=500, height=500, highlightthickness=0, borderwidth=0)
        self.canvas.configure(bg='#FFFFFF')
        self.canvas.pack()

        # Create and place balls onto the canvas.
        pa.generate_random_balls(self.canvas, self.balls)

        self.user_ball_pos_1 = np.array([0, 0])
        self.user_ball_pos_2 = np.array([0, 0])
        self.user_ball_radius = 0

        # Listen to LMB click and drag on canvas.
        self.canvas.bind('<Button-1>', self.lmb_click)
        self.canvas.bind("<B1-Motion>", self.lmb_drag)

    # Create a new ball where the LMB was clicked.
    def lmb_click(self, event):

        self.user_ball_pos_1[0] = event.x
        self.user_ball_pos_1[1] = event.y

        self.user_ball_display = self.canvas.create_oval(self.user_ball_pos_1[0] - self.user_ball_radius, self.user_ball_pos_1[1] - self.user_ball_radius, self.user_ball_pos_2[1] + self.user_ball_radius, self.user_ball_pos_2[1] + self.user_ball_radius, width=0)

        # See: https://stackoverflow.com/questions/50126720/how-do-i-make-lines-by-clicking-dragging-and-releasing-the-mouse-on-tkinter

    # Update ball radius where LMB was dragged.
    def lmb_drag(self, event):

        self.user_ball_pos_2[0] = event.x
        self.user_ball_pos_2[1] = event.y

        # Length of hypotenuse of x2 - x1 and y2 - y1
        self.user_ball_radius = np.hypot(self.user_ball_pos_2[0] - self.user_ball_pos_1[0], self.user_ball_pos_2[1] - self.user_ball_pos_1[1])

        #self.user_ball_display

    def lmb_release(self, event):

        pa.place_ball(self, self.canvas, self.user_ball_pos_1, np.array([0, 0]), self.user_ball_radius, 1)

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

            # Move the ball internally
            ball.pos += ball.vel
            # Move the ball visually
            self.canvas.moveto(ball.image, ball.pos[0] - ball.rad, ball.pos[1] - ball.rad)

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

        # TODO: wall collision works but leans to the bottom-right
        for ball in self.balls:

            if ball.pos[0] - ball.rad < 0:
                ball.pos[0] = ball.rad
                ball.vel[0] = -ball.vel[0]

            if ball.pos[0] + ball.rad > 500:
                ball.pos[0] = 500 - ball.rad
                ball.vel[0] = -ball.vel[0]

            if ball.pos[1] - ball.rad < 0:
                ball.pos[1] = ball.rad
                ball.vel[1] = -ball.vel[1]

            if ball.pos[1] + ball.rad > 500:
                ball.pos[1] = 500 - ball.rad
                ball.vel[1] = -ball.vel[1]