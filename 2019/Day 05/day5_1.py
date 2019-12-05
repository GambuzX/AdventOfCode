with open('input.txt', 'r') as handle:
    numbers = handle.read().split(',')

numbers = [int(n) for n in numbers]


def run_program(nums):
    i = 0
    while nums[i] != 99:
        instr = nums[i] % 100
        op1_mode = int(nums[i] / 100) % 10
        op2_mode = int(nums[i] / 1000) % 10 if instr < 3 else None
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
            nums[nums[i + 1]] = int(input(""))
            i += 2
        elif instr == 4:
            print(op1)
            i += 2
        else:
            print("Unknown instruction")


run_program(numbers)
