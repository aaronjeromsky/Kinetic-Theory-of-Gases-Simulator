import tkinter as tk
import simulation_window as si
import statistics_window as st
import control_window as co
import variables as va

statistics_window = tk.Tk()
simulation_window = tk.Tk()
control_window = tk.Tk()

simulation_object = si.Simulation(simulation_window)
statistics_object = st.Statistics(statistics_window, simulation_object)
control_object = co.Controls(control_window)

# Ball movement is noticebly "glitchy", this is easier to spot with the lowered tick rate.
# TODO: stop all loops when paused (currently using messy workaround)
def update_statistics():

    if (not va.paused):
        statistics_object.update()
    statistics_window.after(va.milliseconds_per_update, update_statistics)

def update_simulation():

    if (not va.paused):
        simulation_object.update()
    simulation_window.after(va.milliseconds_per_tick, update_simulation)

def close_windows():

    statistics_window.destroy()
    simulation_window.destroy()
    control_window.destroy()

if __name__ == '__main__':

    statistics_window.after(va.milliseconds_per_update, update_statistics)
    simulation_window.after(va.milliseconds_per_tick, update_simulation)

    statistics_window.protocol("WM_DELETE_WINDOW", close_windows)
    simulation_window.protocol("WM_DELETE_WINDOW", close_windows)
    control_window.protocol("WM_DELETE_WINDOW", close_windows)

    statistics_window.mainloop()
    simulation_window.mainloop()
    control_window.mainloop()