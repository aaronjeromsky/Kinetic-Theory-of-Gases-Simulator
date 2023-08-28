import tkinter as tk
import variables as va

class Statistics:

    def __init__(self, window):

        # Window
        self.window = window

        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 300
        wh = 400

        x = (sw / 2) - (ww / 2) - 250
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Statistics')
        window.config(background='#FFFFFF')
        icon = tk.PhotoImage(file='icon.png')
        window.iconphoto(True, icon)

        # Labels
        self.stat1label = tk.Label(self.window, text="Seconds per tick: "    + str(va.seconds_per_tick),    font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)
        self.stat2label = tk.Label(self.window, text="Dimension: "           + str(va.dimension),           font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)
        self.stat3label = tk.Label(self.window, text="Pixel to unit ratio: " + str(va.pixel_to_unit_ratio), font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)
        self.stat4label = tk.Label(self.window, text="Number of balls: "     + str(va.number_of_balls),     font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)
        self.stat5label = tk.Label(self.window, text="Maximum radius: "      + str(va.maximum_radius),      font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)
        self.stat6label = tk.Label(self.window, text="Maximum velocity: "    + str(va.maximum_velocity),    font=('Consolas', 16), borderwidth=1, relief=tk.SOLID)

        # Positions
        self.stat1label.place(x=0, y=0)
        self.stat2label.place(x=0, y=28)
        self.stat3label.place(x=0, y=56)
        self.stat4label.place(x=0, y=84)
        self.stat5label.place(x=0, y=112)
        self.stat6label.place(x=0, y=140)

    def update(self):

        # Labels
        self.stat1label['text'] = "Seconds per tick: "    + str(va.seconds_per_tick)
        self.stat2label['text'] = "Dimension: "           + str(va.dimension)
        self.stat3label['text'] = "Pixel to unit ratio: " + str(va.pixel_to_unit_ratio)
        self.stat4label['text'] = "Number of balls: "     + str(va.number_of_balls)
        self.stat5label['text'] = "Maximum radius: "      + str(va.maximum_radius)
        self.stat6label['text'] = "Maximum velocity: "    + str(va.maximum_velocity)