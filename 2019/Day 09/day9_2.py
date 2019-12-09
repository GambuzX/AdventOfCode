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


def run_program(nums):
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
            nums[op1] = int(input(""))
            i += 2
        elif instr == 4:
            print(nums[op1])
            i += 2
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

with open('input.txt', 'r') as handle:
    file_nums = handle.read().split(',')

numbers = {}
for i in range(len(file_nums)):
    numbers[i] = int(file_nums[i])

run_program(numbers)
