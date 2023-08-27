import tkinter as tk
import simulation_window as si
import statistics_window as st

# TODO: sometimes when balls collide they get stuck in eachother, add a check/response for that.

# TODO: when creating two or more balls (via LMB), an error occurs:
# File "c:\Users\Aaron\Documents\Projects\Kinetic-Theory-of-Gases-Simulator\particles.py", line 44, in tooClose
#     return np.linalg.norm(pos1 - pos2) <= radius1 + radius2
#                           ~~~~~^~~~~~
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

milliseconds_per_tick = 10
seconds_per_tick = milliseconds_per_tick / 1000
dimension = 2
pixel_to_unit_ratio = 500
number_of_balls = 5
maximum_radius = 0.1
maximum_velocity = 1

# TODO: make both windows close at the same time.
statistics_window = tk.Tk()
simulation_window = tk.Toplevel()

statistics_object = st.Statistics(statistics_window, seconds_per_tick, dimension, pixel_to_unit_ratio,
                                  number_of_balls, maximum_radius, maximum_velocity)
simulation_object = si.Simulation(simulation_window, seconds_per_tick, dimension, pixel_to_unit_ratio,
                                  number_of_balls, maximum_radius, maximum_velocity)

def update_statistics():

    statistics_object.update(seconds_per_tick, dimension, pixel_to_unit_ratio,
                             number_of_balls, maximum_radius, maximum_velocity)
    statistics_window.after(1000, update_statistics)

def update_simulation():

    simulation_object.update()
    simulation_window.after(milliseconds_per_tick, update_simulation)

if __name__ == '__main__':

    simulation_window.after(milliseconds_per_tick, update_simulation)
    statistics_window.after(1000, update_statistics)

    simulation_window.mainloop()
    statistics_window.mainloop()