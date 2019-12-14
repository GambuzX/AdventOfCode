import re
import math

class Resource:
    def __init__(self, amount, chemical):
        self.amount = amount
        self.chemical = chemical

class Formula:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

with open('input.txt', 'r') as handle:
    lines = handle.read().split('\n')

formulas = {}

for line in lines:
    matches = re.finditer(r"(\d+\s\w+)", line, re.MULTILINE)
    inps = []
    outp = None
    for match in matches:
        ele = match.group()
        separated = re.match(r"(\d+)\s(\w+)", ele)
  
        new_res = Resource(int(separated[1]), separated[2])

        outp = new_res
        inps.append(new_res)

    inps.pop()

    formulas[outp.chemical] = Formula(inps, outp)

def calculate_ore_amount(required_fuel):
    ore_amount = 0
    available_resources = {}
    required = [Resource(required_fuel, 'FUEL')]

    while len(required) > 0:
        
        next = required[-1]
        required.pop()

        if next.chemical not in available_resources.keys():
            available_resources[next.chemical] = 0

        if available_resources[next.chemical] >= next.amount:
            available_resources[next.chemical] -= next.amount
            continue
        elif available_resources[next.chemical] > 0:
            next.amount -= available_resources[next.chemical]
            available_resources[next.chemical] = 0

        # formula which results in this chemical
        formula = formulas[next.chemical]

        formula_times = math.ceil(next.amount / formula.output.amount)
        available_resources[next.chemical] += (formula.output.amount*formula_times - next.amount)

        missing = [Resource(inp.amount*formula_times, inp.chemical) for inp in formula.inputs]

        # add missing eles to required
        for missing_res in missing:
            if missing_res.chemical == "ORE":
                ore_amount += missing_res.amount
            else:
                repeated = False
                for ele_i, ele in enumerate(required):
                    if ele.chemical == missing_res.chemical:
                        repeated = True
                        required[ele_i].amount += missing_res.amount
                        break
                if not repeated:
                    required.append(missing_res)

        
    return ore_amount

limit = 1000000000000
l = 0
r = 999999998
while l <= r:
    mid = l + int((r-l)/2)

    curr_fuel = mid
    curr_ores = calculate_ore_amount(curr_fuel)

    if curr_ores < limit and calculate_ore_amount(curr_fuel+1) > limit:
        print(curr_fuel)
        exit(0)

    elif curr_ores < limit:
        l = mid + 1
    else:
        r = mid - 1

print("did not find solution")

