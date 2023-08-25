import tkinter as tk

# Statistics ideas: dimension, bounds, numballs, max radius, genmaxvel

class Statistics:
    def __init__(self, window, numBalls):

        # Variables
        self.numBalls = numBalls

        # Window
        self.window = window
        self.stat1label = tk.Label(self.window, text=numBalls, font=('Arial', 16), borderwidth=1, relief=tk.SOLID)
        self.stat1label.place(x=0, y=0)

        # Setup
        window.geometry('240x480')
        window.title('Statistics')
        window.config(background='#FFFFFF')
        icon = tk.PhotoImage(file='icon.png')
        window.iconphoto(True, icon)

    # try the after method for updating
    def update(self, numBalls):

        self.stat1label['text'] = numBalls