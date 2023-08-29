import tkinter as tk
import variables as va
import numpy as np

class Statistics:

    def __init__(self, window, sim):

        # not sure this is okay but it works
        self.sim = sim

        # Window
        self.window = window

        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 400
        wh = 400

        x = (sw / 2) - (ww / 2) - 250
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Statistics')
        window.config(background='#FFFFFF')
        icon = tk.PhotoImage(file='icon.png')
        window.iconphoto(True, icon)

        label_font = ('Consolas', 16)

        # Labels
        self.stat1label = tk.Label(self.window, text="Seconds per tick: "    + str(va.seconds_per_tick),                                                                     font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat2label = tk.Label(self.window, text="Dimension: "           + str(va.dimension),                                                                            font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat3label = tk.Label(self.window, text="Pixel to unit ratio: " + str(va.pixel_to_unit_ratio),                                                                  font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat4label = tk.Label(self.window, text="Number of balls: "     + str(va.number_of_balls),                                                                      font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat5label = tk.Label(self.window, text="Maximum radius: "      + str(va.maximum_radius),                                                                       font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat6label = tk.Label(self.window, text="Maximum initial vel: " + str(va.max_gen_units_per_sec),                                                                font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat7label = tk.Label(self.window, text="Average vel: "         + "{:.4f}".format(va.avg_vel[0] * 10000) + ", " + "{:.4f}".format(va.avg_vel[1] * 10000) + "]", font=label_font, borderwidth=1, relief=tk.SOLID)
        self.stat8label = tk.Label(self.window, text="Average speed: "       + "{:.4f}".format(va.avg_vel_mag * 10000),                                                      font=label_font, borderwidth=1, relief=tk.SOLID)

        # Positions
        self.stat1label.place(x=0, y=0)
        self.stat2label.place(x=0, y=28)
        self.stat3label.place(x=0, y=56)
        self.stat4label.place(x=0, y=84)
        self.stat5label.place(x=0, y=112)
        self.stat6label.place(x=0, y=140)
        self.stat7label.place(x=0, y=168)
        self.stat8label.place(x=0, y=196)

    def update(self):

        # Calculate stats
        va.avg_vel = self.sim.return_avg_vel()
        va.avg_vel_mag = np.linalg.norm(va.avg_vel)

        # Labels
        # TODO: velocity values are extremely small, this makes displaying them difficult, can they be bigger?
        self.stat1label['text'] = "Seconds per tick: "    + str(va.seconds_per_tick)
        self.stat2label['text'] = "Dimension: "           + str(va.dimension)
        self.stat3label['text'] = "Pixel to unit ratio: " + str(va.pixel_to_unit_ratio)
        self.stat4label['text'] = "Number of balls: "     + str(va.number_of_balls)
        self.stat5label['text'] = "Maximum radius: "      + str(va.maximum_radius)
        self.stat6label['text'] = "Maximum initial vel: " + str(va.max_gen_units_per_sec)
        self.stat7label['text'] = "Average vel: ["        + "{:.4f}".format(va.avg_vel[0] * 10000) + ", " + "{:.4f}".format(va.avg_vel[1] * 10000) + "]"
        self.stat8label['text'] = "Average speed: "       + "{:.4f}".format(va.avg_vel_mag * 10000)