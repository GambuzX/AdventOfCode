with open('input.txt', 'r') as handle:
	numbers = handle.read().split(',')

numbers = [int(n) for n in numbers]

def run_program(numbers):
	i = 0
	while numbers[i] != 99:
		op1 = numbers[numbers[i+1]]
		op2 = numbers[numbers[i+2]]

		numbers[numbers[i+3]] = (op1+op2 if numbers[i] == 1 else op1*op2)
		i += 4

for noun in range(100):
	for verb in range(100):
		mem = numbers.copy()
		mem[1] = noun
		mem[2] = verb

		run_program(mem)

		if mem[0] == 19690720:
			print(100 * noun + verb)
			exit()
