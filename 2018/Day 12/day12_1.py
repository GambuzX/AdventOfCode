import re

file = open("input.txt")

plants_state = ['.'] * 500
rules = []
zero_offset = 250
last_hash_index = 0
for line in file:
    if "initial state" in line:
        state = re.search("(state:\s)([.#]*)", line).group(2)
        for i in range(len(state)):
            plants_state[zero_offset + i] = state[i]
            if state[i] == '#':
                last_hash_index = i
    elif "=>" in line:
        rules.append(line[:-1:])
file.close()


def rule_matches_pos(rule, pos):
    for i in range(5):
        if rule[i] != pos[i]:
            return False
    return True


n_generations = 20
left_limit = zero_offset - 5
right_limit = last_hash_index + zero_offset + 5
for gen in range(n_generations):

    changes = {}
    for pos in range(left_limit, right_limit+1):
        for rule in rules:
            if rule_matches_pos(rule, plants_state[pos-2:pos+3:]):
                changes[pos] = rule[-1]
                break

    found_first_hash = False
    first_hash_index = -1
    last_hash_index = -1
    for change in changes:
        plants_state[change] = changes[change]
        if changes[change] == '#':
            last_hash_index = change
            if not found_first_hash:
                first_hash_index = change
                found_first_hash = True
    left_limit = first_hash_index - 5
    right_limit = last_hash_index + 5

sum = 0
for i in range(left_limit, right_limit+1):
    if plants_state[i] == '#':
        sum += (i - zero_offset)

print(sum)