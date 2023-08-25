import tkinter as tk
import simulation_window as si
import statistics_window as st

testVariable = 100
secondsPerTick = 0.01
dimension = 2
pixelToUnitRatio = 500
numBalls = 100
maxRadius = 0.5
genMaxVel = 0.5

statistics_window = tk.Tk()
simulation_window = tk.Toplevel()

statistics_object = st.Statistics(statistics_window, testVariable)
simulation_object = si.Simulation(simulation_window, secondsPerTick, dimension,
                                  pixelToUnitRatio, numBalls, maxRadius, genMaxVel)

def updateStatistics():

    global testVariable

    testVariable += 1

    statistics_object.update(testVariable)
    statistics_window.after(1000, updateStatistics)

def updateSimulation():

    simulation_object.update()
    simulation_window.after(10, updateSimulation)


if __name__ == '__main__':

    simulation_window.after(10, updateSimulation)
    statistics_window.after(1000, updateStatistics)

    simulation_window.mainloop()
    statistics_window.mainloop()