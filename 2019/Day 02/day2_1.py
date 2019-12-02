with open('input.txt', 'r') as handle:
	numbers = handle.read().split(',')

numbers = [int(n) for n in numbers]

numbers[1] = 12
numbers[2] = 2

i = 0
while numbers[i] != 99:
	op1 = numbers[numbers[i+1]]
	op2 = numbers[numbers[i+2]]

	numbers[numbers[i+3]] = (op1+op2 if numbers[i] == 1 else op1*op2)
	i += 4

print(numbers[0])