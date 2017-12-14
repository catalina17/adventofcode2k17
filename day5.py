f = open("day5.txt", "r")

instrs = []
for line in f.readlines():
    instrs.append(int(line.split()[0]))

idx = 0
steps = 0
while True:
    jumps = instrs[idx]
    if jumps < 3:
        instrs[idx] += 1
    else:
        instrs[idx] -= 1
    idx += jumps
    steps += 1

    if idx < 0 or idx >= len(instrs):
        print(steps)
        break
