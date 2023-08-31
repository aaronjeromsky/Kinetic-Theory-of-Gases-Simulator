SEC_PER_MS = 0.001
milliseconds_per_update = 17
milliseconds_per_tick = 17
seconds_per_tick = milliseconds_per_tick / 1000

dimension = 2
pixel_to_unit_ratio = 500
number_of_balls = 10

maximum_radius = 0.1
bouncing_fudge_factor = 0.001
collision_tick_fudge_factor = 0.01

#maximum velocity a ball will generate with in units per sec
max_gen_units_per_sec = 0.5

#maximum velocity a ball will generate with in units per tick
max_gen_units_per_tick = max_gen_units_per_sec * SEC_PER_MS * milliseconds_per_tick

#collected stats
avg_vel = None
avg_vel_mag = None

# visuals
text_font = ('Consolas', 16)

# controls
paused = False