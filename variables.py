import numpy as np

# time
SEC_PER_MS = 0.001
milliseconds_per_update = 10
milliseconds_per_tick = 10
seconds_per_tick = milliseconds_per_tick / 1000

# environment
dimension = 2
num_balls = 0
balls_to_create = 50

# statistics
avg_rad = 0
avg_den = 0
avg_vel = np.array([0, 0])
avg_spd = 0

# visuals
text_font = ('Consolas', 16)

# controls
paused = False