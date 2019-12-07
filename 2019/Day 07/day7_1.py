import itertools

with open('input.txt', 'r') as handle:
    numbers = handle.read().split(',')

numbers = [int(n) for n in numbers]


def supports_second_arg(instr):
    return instr != 3 and instr != 4


def run_program(nums, phase, input_signal):
    i = 0
    first_input = True
    ret_signal = 0
    while nums[i] != 99:
        instr = nums[i] % 100
        op1_mode = int(nums[i] / 100) % 10
        op2_mode = int(nums[i] / 1000) % 10 if supports_second_arg(instr) else None
        # op3_mode = int(instr / 10000) % 10 if instr < 3 else None

        op1 = nums[nums[i + 1]] if op1_mode == 0 else nums[i + 1]
        op2 = nums[nums[i + 2]] if op2_mode == 0 else nums[i + 2]

        if instr == 1:
            nums[nums[i + 3]] = op1 + op2
            i += 4
        elif instr == 2:
            nums[nums[i + 3]] = op1 * op2
            i += 4
        elif instr == 3:
            next_inp = phase if first_input else input_signal
            first_input = False
            nums[nums[i + 1]] = next_inp #input
            i += 2
        elif instr == 4:
            ret_signal = op1 # output
            i += 2
        elif instr == 5:
            if op1 != 0:
                i = op2
            else:
                i += 3
        elif instr == 6:
            if op1 == 0:
                i = op2
            else:
                i += 3
        elif instr == 7:
            nums[nums[i + 3]] = 1 if op1 < op2 else 0
            i += 4
        elif instr == 8:
            nums[nums[i + 3]] = 1 if op1 == op2 else 0
            i += 4
        else:
            print("Unknown instruction")

    return ret_signal

def run_circuit(numbers, phase_sequence):
    input_signal = 0
    for phase in phase_sequence:
        nums = numbers.copy()
        input_signal = run_program(nums, phase, input_signal)
    return input_signal


max_found = 0
permutations = list(itertools.permutations([0,1,2,3,4]))
for perm in permutations:
    res = run_circuit(numbers, perm)
    max_found = max(max_found, res)

print(max_found)