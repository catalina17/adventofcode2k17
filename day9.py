import re


def sum_groups(inp, depth):
    global total
    global pos

    total += depth
    print("depth " + str(depth) + " at pos " + str(pos))

    if pos >= len(inp):
        return

    while pos < len(inp):
        pos += 1
        if inp[pos] == '{':
            print("new { at pos " + str(pos))
            sum_groups(inp, depth + 1)
        else:
            return


f = open("day9.txt", "r")
inp = f.readline()

# Replace cancelled characters
while True:
    excl_pos = inp.find("!")
    # No more !s
    if excl_pos == -1:
        break
    inp = inp[:excl_pos] + 'a' + inp[excl_pos + 1:]
    if excl_pos + 1 < len(inp):
        inp = inp[:excl_pos + 1] + 'a' + inp[excl_pos + 2:]

# Delete garbage
while True:
    garbage_begin = inp.find("<")
    # No more to delete
    if garbage_begin == -1:
        break

    garbage_end = inp.find(">")
    inp = inp[:garbage_begin] + inp[garbage_end + 1:]

inp = inp.replace(",", "")
inp = inp.strip()
print(inp)

total = 0
pos = 0

sum_groups(inp, 1)
print(total)
