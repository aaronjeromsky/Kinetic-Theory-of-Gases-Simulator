import tkinter as tk
import variables as va

class Controls:

    def __init__(self, window):

        # Window
        self.window = window

        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        ww = 400
        wh = 200

        x = (sw / 2) - (ww / 2)
        y = (sh / 2) - (wh / 2) - 200

        window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))

        window.title('Statistics')
        window.config(background='#FFFFFF')
        window.resizable(False, False)

        # Buttons
        self.pause_and_play_button = tk.Button(self.window, text="Playing", font=va.text_font, borderwidth=1, relief=tk.SOLID, command=self.pause_and_play_clicked)

        # Positions
        self.pause_and_play_button.place(x=0, y=0)

    def pause_and_play_clicked(self):
        # Change False to True and vice-versa.
        if va.paused == False:
            va.paused = True
            self.pause_and_play_button['text'] = "Paused"
        else:
            va.paused = False
            self.pause_and_play_button['text'] = "Playing"