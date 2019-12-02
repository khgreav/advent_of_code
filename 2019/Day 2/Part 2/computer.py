with open('inputs') as inputs:
    reset = inputs.read().split(",")
inputs.close()

for i in range(0, len(reset)):
    reset[i] = int(reset[i])

for noun in range(100):
    for verb in range(100):
        ops = reset.copy()
        ops[1] = noun
        ops[2] = verb
        for op in range(0, len(ops) - 1, 4):
            if ops[op] == 1:
                ops[ops[op + 3]] = ops[ops[op + 1]] + ops[ops[op + 2]]
            elif ops[op] == 2:
                ops[ops[op + 3]] = ops[ops[op + 1]] * ops[ops[op + 2]]
            elif ops[op] == 99:
                break
        if ops[0] == 19690720:
            print("noun: " + str(noun) + ", verb: " + str(verb))
