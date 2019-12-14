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
available_resources = {}

for line in lines:
    matches = re.finditer(r"(\d+\s\w+)", line, re.MULTILINE)
    inps = []
    outp = None
    for match in matches:
        ele = match.group()
        separated = re.match(r"(\d+)\s(\w+)", ele)
  
        new_res = Resource(int(separated[1]), separated[2])

        if new_res.chemical not in available_resources.keys():
            available_resources[new_res.chemical] = 0

        outp = new_res
        inps.append(new_res)

    inps.pop()

    formulas[outp.chemical] = Formula(inps, outp)
    
ore_amount = 0
required = [formulas['FUEL'].output]

while len(required) > 0:
    
    next = required[-1]
    required.pop()

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

print(ore_amount)
