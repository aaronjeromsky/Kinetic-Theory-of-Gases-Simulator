import tkinter as tk
import simulation_window as si
import statistics_window as st

testVariable = 100
milliSecPerTick = 1
secondsPerTick = milliSecPerTick / 1000
dimension = 2
pixelToUnitRatio = 500
numBalls = 7
maxRadius = 0.1
genMaxVel = 1

statistics_window = tk.Tk() # How does window priority work? Also can you close at the same time?
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
    simulation_window.after(milliSecPerTick, updateSimulation)    # 1000 = 1 sec

if __name__ == '__main__':

    simulation_window.after(milliSecPerTick, updateSimulation)
    statistics_window.after(1000, updateStatistics)

    simulation_window.mainloop()
    statistics_window.mainloop()