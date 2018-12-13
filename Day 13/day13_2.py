import re

file = open("input.txt")


class Cart:
    def __init__(self, direction, choice, prevSymbol):
        self.dir = direction
        self.choice = choice
        self.prevSymbol = prevSymbol


paths = []

total_cars = 0
for line in file:
    line_list = []
    for c in line[:-1:]:
        if c == '>' or c == '<' or c == 'v' or c == '^':
            prev = ''
            if c == '>' or c == '<':
                prev = '-'
            else:
                prev = '|'
            line_list.append(Cart(c, 0, prev))
            total_cars += 1
        else:
            line_list.append(c)
    paths.append(line_list)
file.close()

while True:

    ignore_list = []
    for line in range(len(paths)):
        for col in range(len(paths[0])):
            current = paths[line][col]

            if [col, line] in ignore_list or type(current) is str:
                continue

            if current.dir == '>':
                ignore_list.append([col+1, line])
                next = paths[line][col + 1]
                if type(next) is not str:
                    paths[line][col + 1] = paths[line][col + 1].prevSymbol
                    total_cars -= 2

                elif next == '-':
                    paths[line][col + 1] = Cart('>', current.choice, next)
                elif next == '\\':
                    paths[line][col + 1] = Cart('v', current.choice, next)
                elif next == '/':
                    paths[line][col + 1] = Cart('^', current.choice, next)
                elif next == '+':
                    if current.choice == 0:
                        paths[line][col + 1] = Cart('^', 1, next)
                    elif current.choice == 1:
                        paths[line][col + 1] = Cart('>', 2, next)
                    elif current.choice == 2:
                        paths[line][col + 1] = Cart('v', 0, next)

            elif current.dir == '<':
                ignore_list.append([col-1, line])
                next = paths[line][col - 1]
                if type(next) is not str:
                    paths[line][col - 1] = paths[line][col - 1].prevSymbol
                    total_cars -= 2

                elif next == '-':
                    paths[line][col - 1] = Cart('<', current.choice, next)
                elif next == '\\':
                    paths[line][col - 1] = Cart('^', current.choice, next)
                elif next == '/':
                    paths[line][col - 1] = Cart('v', current.choice, next)
                elif next == '+':
                    if current.choice == 0:
                        paths[line][col - 1] = Cart('v', 1, next)
                    elif current.choice == 1:
                        paths[line][col - 1] = Cart('<', 2, next)
                    elif current.choice == 2:
                        paths[line][col - 1] = Cart('^', 0, next)
            elif current.dir == 'v':
                ignore_list.append([col, line+1])
                next = paths[line + 1][col]
                if type(next) is not str:
                    paths[line + 1][col] = paths[line + 1][col].prevSymbol
                    total_cars -= 2

                elif next == '|':
                    paths[line + 1][col] = Cart('v', current.choice, next)
                elif next == '\\':
                    paths[line + 1][col] = Cart('>', current.choice, next)
                elif next == '/':
                    paths[line + 1][col] = Cart('<', current.choice, next)
                elif next == '+':
                    if current.choice == 0:
                        paths[line + 1][col] = Cart('>', 1, next)
                    elif current.choice == 1:
                        paths[line + 1][col] = Cart('v', 2, next)
                    elif current.choice == 2:
                        paths[line + 1][col] = Cart('<', 0, next)
            elif current.dir == '^':
                ignore_list.append([col, line-1])
                next = paths[line - 1][col]
                if type(next) is not str:
                    paths[line - 1][col] = paths[line - 1][col].prevSymbol
                    total_cars -= 2

                elif next == '|':
                    paths[line - 1][col] = Cart('^', current.choice, next)
                elif next == '\\':
                    paths[line - 1][col] = Cart('<', current.choice, next)
                elif next == '/':
                    paths[line - 1][col] = Cart('>', current.choice, next)
                elif next == '+':
                    if current.choice == 0:
                        paths[line - 1][col] = Cart('<', 1, next)
                    elif current.choice == 1:
                        paths[line - 1][col] = Cart('^', 2, next)
                    elif current.choice == 2:
                        paths[line - 1][col] = Cart('>', 0, next)
            paths[line][col] = current.prevSymbol
    if total_cars == 1:
        for line in range(len(paths)):
            for col in range(len(paths[0])):
                if type(paths[line][col]) is not str:
                    print("Last car at " + str(col) + " " + str(line))
        break