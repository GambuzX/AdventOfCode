with open("input.txt", 'r') as handle:
	pwds = handle.read().split('-')

first = int(pwds[0])
last = int(pwds[1])

def valid_pwd(pwd):
	pwd_str = str(pwd)

	if len(pwd_str) != 6:
		return False

	if pwd < first or pwd > last:
		return False

	found_double = False
	last_c = pwd_str[0]
	for i in range(1, len(pwd_str)):
		c = pwd_str[i]

		if int(c) < int(last_c):
			return False

		if c == last_c:
			found_double = True

		last_c = c

	return found_double


count = 0
for num in range(first, last+1):
	if valid_pwd(num):
		count += 1
print(count) 