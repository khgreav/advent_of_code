with open('inputs') as inputs:
    ops = inputs.read().split(",")
inputs.close()

for i in range(0, len(ops)):
    ops[i] = int(ops[i])

ops[1] = 12
ops[2] = 2

for op in range(0, len(ops)-1, 4):
    if ops[op] == 1:
        ops[ops[op+3]] = ops[ops[op+1]] + ops[ops[op+2]]
    elif ops[op] == 2:
        ops[ops[op+3]] = ops[ops[op+1]] * ops[ops[op+2]]
    elif ops[op] == 99:
        break

print(ops[0])