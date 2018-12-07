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

instructions_order = ""


def remove_from_requirements(char):
    for c in range(ord('A'), ord('Z') + 1):
        try:
            requirements[chr(c)].remove(char)
        except ValueError:
            pass


while(len(instructions_order) < 26):
    for code in range(ord('A'), ord('Z')+1):
        char = chr(code)
        if char not in instructions_order and len(requirements[char]) == 0:
            instructions_order += char
            remove_from_requirements(char)
            break

print(instructions_order)
