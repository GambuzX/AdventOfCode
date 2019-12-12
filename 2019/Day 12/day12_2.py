import re
from math import gcd

def position_diff(val1, val2):
    if val1 > val2:
        return 1
    
    if val2 > val1:
        return -1
    
    return 0

class Moon:
    def __init__(self, id, initial_pos):
        self.id = id
        self.position = initial_pos
        self.velocity = [0, 0, 0]

def moons_dim(moons, dim):
    return [[moon.position[dim], moon.velocity[dim]] for moon in moons]

def evolve_dimension(dimension_vals):
    for moon_i, moon in enumerate(dimension_vals):
        for other in dimension_vals[moon_i+1:]:
            #determine increment
            inc = 1 if moon[0] < other[0] else -1 if moon[0] > other[0] else 0

            #update velocity
            moon[1], other[1] = moon[1] + inc, other[1] - inc
    #update positions
    for moon in dimension_vals:
        moon[0] += moon[1]

    return dimension_vals

def steps_to_loop(initial_dim):
    step = 1
    curr_vals = [d[:] for d in initial_dim]
    while evolve_dimension(curr_vals) != initial_dim:
        step += 1
    return step

def lcm(a,b):
    return a*b//gcd(a,b)

with open('input.txt', 'r') as handle:
    lines = handle.read().split('\n')

moons = []
for i in range(len(lines)):
    vals = re.match(r'<x=(.*),\sy=(.*),\sz=(.*)>', lines[i])
    x = int(vals[1])
    y = int(vals[2])
    z = int(vals[3])
    moons.append(Moon(i, [x,y,z]))


x_loop = steps_to_loop(moons_dim(moons, 0))
y_loop = steps_to_loop(moons_dim(moons, 1))
z_loop = steps_to_loop(moons_dim(moons, 2))

print(lcm(lcm(x_loop, y_loop), z_loop))