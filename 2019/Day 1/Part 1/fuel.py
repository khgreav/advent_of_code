import math

with open('inputs', 'r') as inputs:
    mass = inputs.readline()
    total_fuel = 0
    while mass:
        total_fuel += math.floor(float(mass)/3) - 2
        mass = inputs.readline()
inputs.close()

print(total_fuel)
