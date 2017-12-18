f = open("day11.txt", "r")
inp = f.readline()

tokens = inp.split(',')
tokens[-1] = tokens[-1][:-1]
print(tokens)

nw_se = 0
n_s = 0
ne_sw = 0
max_dist = 0
for token in tokens:
    if token == "nw":
        nw_se += 1
    elif token == "n":
        n_s += 1
    elif token == "ne":
        ne_sw += 1
    elif token == "sw":
        ne_sw -= 1
    elif token == "s":
        n_s -= 1
    else: # token == "se"
        nw_se -= 1

    max_dist = max(max_dist, abs(n_s) + abs(ne_sw))

print(nw_se, n_s, ne_sw) # (9, -367, -429)
print(max_dist)
