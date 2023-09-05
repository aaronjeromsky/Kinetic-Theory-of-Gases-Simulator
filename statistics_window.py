import tkinter as tk
import variables as va
import os as os

class Statistics:

    def __init__(self, window):

        # Window
        self.window = window

        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 450
        wh = 400

        x = (sw / 2) - (ww / 2) - 300
        y = (sh / 2) - (wh / 2)

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Statistics')
        window.config(background='#FFFFFF')
        window.resizable(False, False)

        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        icon_path = os.path.join(script_dir, 'icon.png')
        icon_image = tk.PhotoImage(file=icon_path)
        window.iconphoto(True, icon_image)

        # Labels
        self.stat1label = tk.Label(self.window, text="Seconds per tick: "  + str(va.seconds_per_tick),                                                     font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat2label = tk.Label(self.window, text="Dimensions: "        + str(va.dimension),                                                            font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat3label = tk.Label(self.window, text="Number of balls: "   + str(va.num_balls),                                                            font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat4label = tk.Label(self.window, text="Average radius: "    + "{:.4f}".format(va.avg_rad),                                                  font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat5label = tk.Label(self.window, text="Average density: "   + "{:.4f}".format(va.avg_den),                                                  font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat6label = tk.Label(self.window, text="Average velocity: [" + "{:.4f}".format(va.avg_vel[0]) + ", " + "{:.4f}".format(va.avg_vel[1]) + "]", font=va.text_font, borderwidth=1, relief=tk.SOLID)
        self.stat7label = tk.Label(self.window, text="Average speed: "     + "{:.4f}".format(va.avg_spd),                                                  font=va.text_font, borderwidth=1, relief=tk.SOLID)

        # Positions
        self.stat1label.place(x=0, y=0)
        self.stat2label.place(x=0, y=28)
        self.stat3label.place(x=0, y=56)
        self.stat4label.place(x=0, y=84)
        self.stat5label.place(x=0, y=112)
        self.stat6label.place(x=0, y=140)
        self.stat7label.place(x=0, y=168)

    def update(self):

        # Labels
        self.stat1label['text'] = "Seconds per tick: "  + str(va.seconds_per_tick)
        self.stat2label['text'] = "Dimensions: "        + str(va.dimension)
        self.stat3label['text'] = "Number of balls: "   + str(va.num_balls)
        self.stat4label['text'] = "Average radius: "    + "{:.4f}".format(va.avg_rad)
        self.stat5label['text'] = "Average density: "   + "{:.4f}".format(va.avg_den)
        self.stat6label['text'] = "Average velocity: [" + "{:.4f}".format(va.avg_vel[0]) + ", " + "{:.4f}".format(va.avg_vel[1]) + "]"
        self.stat7label['text'] = "Average speed: "     + "{:.4f}".format(va.avg_spd)