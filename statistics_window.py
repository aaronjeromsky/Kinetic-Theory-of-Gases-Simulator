import tkinter as tk

class Statistics:

    def __init__(self, window, seconds_per_tick, dimension, pixel_to_unit_ratio, number_of_balls, maximum_radius, maximum_velocity):

        # Variables
        self.seconds_per_tick = seconds_per_tick
        self.dimension = dimension
        self.pixel_to_unit_ratio = pixel_to_unit_ratio
        self.number_of_balls = number_of_balls
        self.maximum_radius = maximum_radius
        self.maximum_velocity = maximum_velocity

        # Window
        self.window = window

        ww = 300
        wh = 400
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()

        x = (sw / 2) - (ww / 2) - 250
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Statistics')
        window.config(background='#FFFFFF')
        icon = tk.PhotoImage(file='icon.png')
        window.iconphoto(True, icon)

        # Labels
        self.stat1label = tk.Label(self.window, text="Second per tick: " + str(seconds_per_tick), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat2label = tk.Label(self.window, text="Dimension: " + str(dimension), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat3label = tk.Label(self.window, text="Pixel to unit ratio: " + str(pixel_to_unit_ratio), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat4label = tk.Label(self.window, text="Number of balls: " + str(number_of_balls), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat5label = tk.Label(self.window, text="Maximum radius: " + str(maximum_radius), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat6label = tk.Label(self.window, text="Maximum velocity: " + str(maximum_velocity), font=('Arial', 16), borderwidth=1, relief=tk.SOLID)

        # Positions
        self.stat1label.place(x=0, y=0)
        self.stat2label.place(x=0, y=28)
        self.stat3label.place(x=0, y=56)
        self.stat4label.place(x=0, y=84)
        self.stat5label.place(x=0, y=112)
        self.stat6label.place(x=0, y=140)

    def update(self, seconds_per_tick, dimension, pixel_to_unit_ratio, number_of_balls, maximum_radius, maximum_velocity):

        # Variables
        self.seconds_per_tick = seconds_per_tick
        self.dimension = dimension
        self.pixel_to_unit_ratio = pixel_to_unit_ratio
        self.number_of_balls = number_of_balls
        self.maximum_radius = maximum_radius
        self.maximum_velocity = maximum_velocity

        # Labels
        self.stat1label['text'] = "Second per tick: " + str(seconds_per_tick)
        self.stat2label['text'] = "Dimension: " + str(dimension)
        self.stat3label['text'] = "Pixel to unit ratio: " + str(pixel_to_unit_ratio)
        self.stat4label['text'] = "Number of balls: " + str(number_of_balls)
        self.stat5label['text'] = "Maximum radius: " + str(maximum_radius)
        self.stat6label['text'] = "Maximum velocity: " + str(maximum_velocity)