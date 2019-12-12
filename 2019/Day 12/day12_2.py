import re

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
        self.compared_to = []
    
    def update_gravity(self, moon2):        
        self.compared_to.append(moon2.id)
        self.velocity[0] += position_diff(moon2.position[0], self.position[0])
        self.velocity[1] += position_diff(moon2.position[1], self.position[1])
        self.velocity[2] += position_diff(moon2.position[2], self.position[2])
    
    def update_position(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def potential_energy(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kinetic_energy(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])
    
    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

def apply_gravity(moons):
    for moon in moons:
        moon.compared_to = []

    for i1 in range(len(moons)):
        for i2 in range(len(moons)):
            if i1 == i2:
                continue
            
            moon1 = moons[i1]
            moon2 = moons[i2]

            # already compared
            if moon1.id in moon2.compared_to:
                continue

            moon1.update_gravity(moon2)
            moon2.update_gravity(moon1)

def apply_velocity(moons):
    for moon in moons:
        moon.update_position()

def system_energy(moons):
    total = 0
    for moon in moons:
        total += moon.total_energy()
    return total



with open('input.txt', 'r') as handle:
    lines = handle.read().split('\n')

moons = []
for i in range(len(lines)):
    vals = re.match(r'<x=(.*),\sy=(.*),\sz=(.*)>', lines[i])
    x = int(vals[1])
    y = int(vals[2])
    z = int(vals[3])
    moons.append(Moon(i, [x,y,z]))

N_STEPS = 1000
for step in range(N_STEPS):
    apply_gravity(moons)
    apply_velocity(moons)

print(system_energy(moons))