from PIL import Image, ImageDraw

class Direction:
    def __init__(self, start_dir):
        self.move = start_dir
    
    def turn_right(self):
        new_move = [self.move[1], self.move[0]]

        if self.move[0] != 0:
            new_move[1] *= -1
        
        self.move = new_move
    
    def turn_left(self):
        new_move = [self.move[1], self.move[0]]

        if self.move[1] != 0:
            new_move[0] *= -1
        
        self.move = new_move

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

    map = {(0,0) : 1}
    curr_pos = (0,0)
    painted_area = 1
    dir = Direction([0,1])

    color_to_paint = None
    new_direction = None

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
            curr_color = 0
            if curr_pos in map.keys():
                curr_color = map[curr_pos]
            nums[op1] = curr_color
            i += 2
        elif instr == 4:
            i += 2
            if color_to_paint == None:
                color_to_paint = nums[op1]
                continue
            else:
                new_direction = nums[op1]

            # paint area
            if curr_pos not in map.keys():
                painted_area += 1
                map[curr_pos] = 0            
            map[curr_pos] = color_to_paint

            # rotate
            if new_direction == 0:
                dir.turn_left()
            else:
                dir.turn_right()

            # advance
            curr_pos = (curr_pos[0] + dir.move[0], curr_pos[1] + dir.move[1])

            # reset values
            color_to_paint = None
            new_direction = None

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
    return map

with open('input.txt', 'r') as handle:
    file_nums = handle.read().split(',')

numbers = {}
for i in range(len(file_nums)):
    numbers[i] = int(file_nums[i])

painted_map = run_program(numbers)

img = Image.new('RGB', (100, 10), "green")
pixels = img.load()

for row in range(10):
    for col in range(100):
        pos = (col-50, row-5)   
        if pos in painted_map.keys() and painted_map[pos] == 1:
            pixels[col, row] = [255,255,255]

img.show()

