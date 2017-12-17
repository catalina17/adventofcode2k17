import re


def swap(p1, p2):
    global program_list
    # Swap programs
    aux = program_list[p1]
    program_list[p1] = program_list[p2]
    program_list[p2] = aux


f = open("day16.txt", "r")
inp = f.readline()

tokens = inp.split(',')
tokens[-1] = tokens[-1][:-1] # get rid of \n
program_list = [(chr(ord('a') + x)) for x in range(0,16)]
init_list = program_list

num_iter = 0
lists = {}
lists[str(init_list)] = 0

while True:
    num_iter += 1

    for token in tokens:
        if token[0] == 's':
            spin_size = int(token[1:])
            # Spin
            program_list = program_list[-spin_size:] + program_list[:-spin_size]
        elif token[0] == 'x':
            to_swap = token[1:].split('/')
            p1 = int(to_swap[0])
            p2 = int(to_swap[1])
            swap(p1, p2)
        else: # token[0] == 'p'
            to_swap = token[1:].split('/')
            # Find positions of programs in list
            p1 = program_list.index(to_swap[0])
            p2 = program_list.index(to_swap[1])
            swap(p1, p2)

    if str(program_list) in lists:
        # We found an already existing permutation
        print(program_list)
        # Find current iteration and length of cycle
        print(num_iter, num_iter - lists[str(program_list)])
        # Find 1000000000th state
        for key in lists:
            if lists[key] == 1000000000 % 48:
                print(key)
                break
        break
    else:
        # Update seen states
        lists[str(program_list)] = num_iter
