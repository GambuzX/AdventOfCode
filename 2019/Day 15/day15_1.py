class PCState:
    def __init__(self, instr, instructions):
        self.instr = 0
        self.instructions = instructions.copy()
        self.finished = False

def supports_second_arg(instr):
    return instr != 3 and instr != 4 and instr != 9

def supports_third_arg(instr):
    return instr == 1 or instr == 2 or instr == 7 or instr == 8

def assure_key_values(nums, i, rel_base):
    if i+1 not in nums.keys():
        nums[i+1] = 0
    if i+2 not in nums.keys():
        nums[i+2] = 0
    if i+3 not in nums.keys():
        nums[i+3] = 0
    if nums[i+1] not in nums.keys():
        nums[nums[i+1]] = 0
    if (nums[i+1]+rel_base) not in nums.keys():
        nums[nums[i+1]+rel_base] = 0
    if nums[i+2] not in nums.keys():
        nums[nums[i+2]] = 0
    if nums[i+3] not in nums.keys():
        nums[nums[i+3]] = 0

def calc_operand_offset(nums, mode, i, rel_base):
    if mode == 0:
        return nums[i]
    elif mode == 1:
        return i
    elif mode == 2:
        return nums[i] + rel_base
    elif mode == None:
        return None
    else:
        print("Unknown mode")


def run_program(pc_state, input_val):

    nums = pc_state.instructions
    i = pc_state.instr

    i = 0
    rel_base = 0
    while nums[i] != 99:
        instr = nums[i] % 100
        op1_mode = int(nums[i] / 100) % 10
        op2_mode = int(nums[i] / 1000) % 10 if supports_second_arg(instr) else None
        op3_mode = int(nums[i] / 10000) % 10 if supports_third_arg(instr) else None

        assure_key_values(nums, i, rel_base)

        op1 = calc_operand_offset(nums, op1_mode, i+1, rel_base)
        op2 = calc_operand_offset(nums, op2_mode, i+2, rel_base)
        op3 = calc_operand_offset(nums, op3_mode, i+3, rel_base)

        if instr == 1:
            nums[op3] = nums[op1] + nums[op2]
            i += 4
        elif instr == 2:
            nums[op3] = nums[op1] * nums[op2]
            i += 4
        elif instr == 3:
            # input
            nums[op1] = input_val
            i += 2
        elif instr == 4:            
            i += 2
            pc_state.instr = i # store instruction pointer
            return nums[op1]
        elif instr == 5:
            if nums[op1] != 0:
                i = nums[op2]
            else:
                i += 3
        elif instr == 6:
            if nums[op1] == 0:
                i = nums[op2]
            else:
                i += 3
        elif instr == 7:
            nums[op3] = 1 if nums[op1] < nums[op2] else 0
            i += 4
        elif instr == 8:
            nums[op3] = 1 if nums[op1] == nums[op2] else 0
            i += 4
        elif instr == 9:
            rel_base += nums[op1]
            i += 2
        else:
            print("Unknown instruction")

    pc_state.finished = True
    pc_state.instr = i
    return -1

dir_increments = {
    1 : (0, 1),
    2 : (0, -1),
    3 : (-1, 0),
    4 : (1, 0)
}

def find_oxygen_system(state, pos, seen, curr_dist):

    best_solution = 99999

    # mark current location as seen
    seen.add(pos)
    
    # check all four directions
    for dir in range(1,5):
        next_pos = (pos[0] + dir_increments[dir][0], pos[1] + dir_increments[dir][1])

        # verify position isnt in search stack
        if next_pos not in seen:
            state_copy = PCState(state.instr, state.instructions)
            move_result = run_program(state_copy, dir)
            if move_result == 2:
                best_solution = min(best_solution, curr_dist+1)
            elif move_result == 1:
                best_solution = min(best_solution, find_oxygen_system(state_copy, next_pos, seen, curr_dist+1))
    
    seen.remove(pos)

    return best_solution


with open('input.txt', 'r') as handle:
    file_nums = handle.read().split(',')

numbers = {}
for i in range(len(file_nums)):
    numbers[i] = int(file_nums[i])

seen = set()
initial_state = PCState(0, numbers)
print(find_oxygen_system(initial_state, (0,0), seen, 0))

