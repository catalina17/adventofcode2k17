f = open("day19.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line)

add_i = 1
add_j = 0
i = 0
j = lines[0].index('|')
chars = ""
steps = 0

while True:
    # Check if we're on a character
    if lines[i][j].isalpha():
        chars += lines[i][j]

    # One step on the path
    i += add_i
    j += add_j
    steps += 1

    # Not on the path anymore
    if i < 0 or j < 0 or i > len(lines) or j > len(lines[i]):
        print "Out of the grid at", i, j
        break
    if not lines[i][j].isalpha() and not lines[i][j] in ['+', '|', '-']:
        print "Out of the grid at", i, j
        break

    # Change direction
    if lines[i][j] == '+':
        # Up
        if i > 0 and add_j != 0 and j < len(lines[i - 1]) and\
           (lines[i - 1][j] == '|' or lines[i - 1][j].isalpha()):
            add_i = -1
            add_j = 0

        # Down
        elif i < len(lines) - 1 and add_j != 0 and j < len(lines[i + 1]) and\
             (lines[i + 1][j] == '|' or lines[i + 1][j].isalpha()):
            add_i = 1
            add_j = 0

        # Left
        elif j > 0 and add_i != 0 and\
             (lines[i][j - 1] == '-' or lines[i][j - 1].isalpha()):
            add_i = 0
            add_j = -1

        # Right
        elif j < len(lines[i]) - 1 and add_i != 0 and\
             (lines[i][j + 1] == '-' or lines[i][j + 1].isalpha()):
            add_i = 0
            add_j = 1

        # No possible step
        else:
            "Can't advance at ", i, j
            break

print chars, steps
