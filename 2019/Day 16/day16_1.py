pattern_seq = {
    0 : 0,
    1 : 1,
    2 : 0,
    3: -1
}

def apply_pattern(nums, nums_len, pos):
    total = 0
    for i in range(len(nums)):
        pattern_char_i = int((i+1)/(pos+1)) % 4
        total += nums[i] * pattern_seq[pattern_char_i]
    return abs(total) % 10

def apply_phase(nums, nums_len):
    new_nums = []

    for pos in range(len(nums)):
        res = apply_pattern(nums, nums_len, pos)
        new_nums.append(res)

    return new_nums

with open('input.txt', 'r') as handle:
    nums = [int(c) for c in handle.read()]

offset = "".join(str(num) for num in nums[:7])
nums_len = len(nums)
for phase in range(100):
    nums = apply_phase(nums, nums_len)

print("".join(str(num) for num in nums[:8]))