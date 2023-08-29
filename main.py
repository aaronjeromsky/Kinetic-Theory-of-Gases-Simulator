import tkinter as tk
import simulation_window as si
import statistics_window as st
import variables as va

# TODO: sometimes when balls collide they get stuck in eachother, add a check/response for that.

statistics_window = tk.Tk()
simulation_window = tk.Tk()

simulation_object = si.Simulation(simulation_window)
statistics_object = st.Statistics(statistics_window, simulation_object)
#I'm passing the simulation_object to stats so that it can so stats on it. I'm not sure this is the best way to do it

def update_statistics():

    statistics_object.update()
    statistics_window.after(va.milliseconds_per_update, update_statistics)

def update_simulation():

    simulation_object.update()
    simulation_window.after(va.milliseconds_per_tick, update_simulation)

def close_windows():

    statistics_window.destroy()
    simulation_window.destroy()

if __name__ == '__main__':

    statistics_window.after(va.milliseconds_per_update, update_statistics)
    simulation_window.after(va.milliseconds_per_tick, update_simulation)

    statistics_window.protocol("WM_DELETE_WINDOW", close_windows)
    simulation_window.protocol("WM_DELETE_WINDOW", close_windows)

    statistics_window.mainloop()
    simulation_window.mainloop()