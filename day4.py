import numpy as np

f = open("day4.txt", "r")

valid = 0
for line in f.readlines():
    words = line.split()

    for i in range(0, len(words)):
        words[i] = ''.join(sorted(words[i]))

    words = np.array(words)
    if len(words) == len(np.unique(words)):
        valid += 1

print(valid)
