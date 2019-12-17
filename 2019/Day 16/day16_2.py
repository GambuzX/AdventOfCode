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

def calc_phase(inp):
	total = sum(inp)
	outp = []
	for i in range(len(inp)):
		outp += [abs(total) % 10]
		total -= inp[i]
	return outp

with open('input.txt', 'r') as handle:
    nums = [int(c) for c in handle.read()]

offset = int("".join([str(c) for c in nums[:7]]))
nums = nums*10000
nums = nums[offset:]

for p in range(100):
    nums = calc_phase(nums)

print("".join(map(str, nums[:8])))
