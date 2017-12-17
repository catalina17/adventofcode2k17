mod = 2147483647
num_iters = 5000000

# Input values
prev_A = 116
prev_B = 299

# Factor values
factor_A = 16807
factor_B = 48271

count = 0
# Run 40M/5M pairs
for i in range(0, num_iters):
    while True:
        val_A = (prev_A * factor_A) % mod
        prev_A = val_A
        if val_A & 3 == 0:
            break
    while True:
        val_B = (prev_B * factor_B) % mod
        prev_B = val_B
        if val_B & 7 == 0:
            break

    # Lowest 16 bits match
    if val_A & ((1<<16) - 1) == val_B & ((1<<16) - 1):
        count += 1
    print(i)

print(count)
