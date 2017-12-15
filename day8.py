f = open("day8.txt", "r")
regs = {}
max_val_proc = 0

for line in f.readlines():
    tokens = line.split()
    r_change = tokens[0]
    r_cond = tokens[4]
    # Add register names to dict if they're not already there
    if not r_change in regs:
        regs[r_change] = 0
    if not r_cond in regs:
        regs[r_cond] = 0
    # Evaluate condition
    truth_value = None
    if tokens[5] == ">":
        truth_value = (regs[r_cond] > int(tokens[6]))
    elif tokens[5] == "<":
        truth_value = (regs[r_cond] < int(tokens[6]))
    elif tokens[5] == "==":
        truth_value = (regs[r_cond] == int(tokens[6]))
    elif tokens[5] == ">=":
        truth_value = (regs[r_cond] >= int(tokens[6]))
    elif tokens[5] == "<=":
        truth_value = (regs[r_cond] <= int(tokens[6]))
    else:
        truth_value = (regs[r_cond] != int(tokens[6]))
    # Modify register if condition evaluated to true
    if truth_value:
        if tokens[1] == "inc":
            regs[r_change] += int(tokens[2])
        else:
            regs[r_change] -= int(tokens[2])

        max_val_proc = max(max_val_proc, regs[r_change])

print(max_val_proc)

max_val = -1<<32
for reg in regs:
    max_val = max(max_val, regs[reg])
print(max_val)
