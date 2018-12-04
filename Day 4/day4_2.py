lines = []

file = open("input.txt");
for line in file:
    lines.append(line[:len(line)-1:])
file.close()


def day(a):
    return a[9:11]


def month(a):
    return a[6:8]


def hour(a):
    return a[12:14]


def minute(a):
    return a[15:17]


def guard_id(a):
    return a[26:30]


def cvn_line(a):
    return month(a) + day(a) + hour(a) + minute(a)


lines = sorted(lines, key=cvn_line)

guards = {}
last_guard = ""
started_sleep = 0
for line in lines:
    if "Guard" in line:
        last_guard = guard_id(line)
        if last_guard in guards:
            continue
        else:
            guards[last_guard] = []
    elif "asleep" in line:
        started_sleep = int(minute(line))
    elif "wakes" in line:
        ended_sleep = int(minute(line))
        for mint in range(started_sleep, ended_sleep):
            guards[last_guard].append(mint)
        started_sleep = 0


most_frequent_sleeper = ""
most_frequent_minute = 0
max_minute_frequency = 0

for guard in guards:
    minutes_slept = {}
    for entry in guards[guard]:
        if entry not in minutes_slept:
            minutes_slept[entry] = 1
        else:
            minutes_slept[entry] += 1

    most_slept_minute = 0
    slept_count = 0
    for mint in minutes_slept:
        if minutes_slept[mint] > slept_count:
            slept_count = minutes_slept[mint]
            most_slept_minute = mint

    if slept_count > max_minute_frequency:
        max_minute_frequency = slept_count
        most_frequent_minute = most_slept_minute
        most_frequent_sleeper = guard

print("Most frequent sleeper guard was " + most_frequent_sleeper)
print("Slept more at minute " + str(most_frequent_minute))
print("Answer is equal to " + str(int(most_frequent_sleeper) * most_frequent_minute))
