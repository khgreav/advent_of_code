import math

with open('inputs', 'r') as inputs:
    mass = inputs.readline()
    total_fuel = 0
    while mass:
        module_fuel = math.floor(float(mass) / 3) - 2

        while module_fuel > 0:
            total_fuel += module_fuel
            module_fuel = math.floor(module_fuel / 3) - 2

        mass = inputs.readline()
inputs.close()

print(total_fuel)