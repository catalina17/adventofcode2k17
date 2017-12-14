f = open("day6.txt", "r")
state = f.readline().split()

# Parse initial state from input file
for i in range(0, len(state)):
    state[i] = int(state[i])

# Add initial state to hashmap
prev_states = {}
prev_states[str(state)] = 1

num_cycles = 0
while True:
    print(state)
    # New redistribution cycle
    num_cycles += 1
    # Get index of bank with max number of blocks
    max_idx = state.index(max(state))
    print("Max blocks at: " + str(max_idx))

    # Calculate increment of blocks for each bank
    inc = state[max_idx] / len(state)
    add_1_more_cnt = state[max_idx] % len(state)
    state[max_idx] = 0

    # Redistribute
    for i in range(0, len(state)):
        state[i] += inc
    for i in range(0, add_1_more_cnt):
        state[(max_idx + 1 + i) % len(state)] += 1

    # Check if we've been in this state before
    if str(state) in prev_states:
        print(state)
        print(num_cycles - prev_states[str(state)])
        break
    else:
        prev_states[str(state)] = num_cycles
