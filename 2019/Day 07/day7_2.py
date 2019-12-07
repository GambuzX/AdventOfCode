import itertools

with open('input.txt', 'r') as handle:
    numbers = handle.read().split(',')

numbers = [int(n) for n in numbers]

class AmplifierState:
    def __init__(self, id, instructions):
        self.id = id
        self.instr = 0
        self.instructions = instructions.copy()
        self.first_input = True
        self.finished = False
        self.initial_phase = 0


def supports_second_arg(instr):
    return instr != 3 and instr != 4


def run_program(amp_state, input_signal):

    nums = amp_state.instructions
    i = amp_state.instr

    used_input = False
    output_signal = 0
    while nums[i] != 99:
        instr = nums[i] % 100
        op1_mode = int(nums[i] / 100) % 10
        op2_mode = int(nums[i] / 1000) % 10 if supports_second_arg(instr) else None

        op1 = nums[nums[i + 1]] if op1_mode == 0 else nums[i + 1]
        op2 = nums[nums[i + 2]] if op2_mode == 0 else nums[i + 2]

        if instr == 1:
            nums[nums[i + 3]] = op1 + op2
            i += 4
        elif instr == 2:
            nums[nums[i + 3]] = op1 * op2
            i += 4
        elif instr == 3:
            # input
            next_inp = amp_state.initial_phase if amp_state.first_input else input_signal

            if not amp_state.first_input:
                # need more input
                if used_input:
                    amp_state.instr = i # store instruction pointer
                    return output_signal # suspend execution
                used_input = True
                
            amp_state.first_input = False
            nums[nums[i + 1]] = next_inp
            i += 2
            
        elif instr == 4:
            output_signal = op1 # output
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

    amp_state.finished = True
    amp_state.instr = i
    return output_signal

def run_circuit(numbers, phase_sequence):
    amplifiers = [AmplifierState(chr(c), numbers) for c in range(ord('A'), ord('A')+len(phase_sequence))]

    # init phase
    for i,amp in enumerate(amplifiers):
        amp.initial_phase = phase_sequence[i]

    next_amp = 0
    prev_output = 0
    count = 0
    while not amplifiers[4].finished:
        prev_output = run_program(amplifiers[next_amp], prev_output)
        next_amp = (next_amp + 1) % len(amplifiers)

    return prev_output


max_found = 0
permutations = list(itertools.permutations([5,6,7,8,9]))
for perm in permutations:
    res = run_circuit(numbers, perm)
    max_found = max(max_found, res)

print(max_found)