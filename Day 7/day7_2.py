import re

file = open("input.txt")
requirements = {}
for char in range(ord('A'), ord('Z')+1):
    requirements[chr(char)] = []

for line in file:
    first = re.search("(Step\s)([A-Z])", line).group(2)
    second = re.search("(step\s)([A-Z])", line).group(2)
    requirements[second].append(first)

file.close()

def remove_from_requirements(char):
    for c in range(ord('A'), ord('Z') + 1):
        try:
            requirements[chr(c)].remove(char)
        except ValueError:
            pass


def time_of_part(char):
    return 60 + ord(char) - ord('A')


def assign_task(workers_l, letter):
    for worker in workers_l:
        if worker[0] == 0 and worker[1] == '#':
            worker[0] = time_of_part(letter)
            worker[1] = letter
            return


def decrement_time(workers_l):
    for worker in workers_l:
        if worker[0] > 0:
            worker[0] -= 1


instructions_order = ""
time = 0
workers = [[0, '#'] for i in range(5)]
tasks_assigned = []
while len(instructions_order) < 26:
    for code in range(ord('A'), ord('Z')+1):
        char = chr(code)
        if char not in instructions_order and char not in tasks_assigned and len(requirements[char]) == 0:
            assign_task(workers, char)
            tasks_assigned.append(char)

    for worker in workers:
        if worker[0] == 0 and worker[1] != '#':
            instructions_order += worker[1]
            remove_from_requirements(worker[1])
            worker[1] = '#'

    decrement_time(workers)
    time += 1


print(time)
