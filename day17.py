steps = 363
buf = [0]
pos = 0

last_at_1 = 1

for i in range(1, 50000001):
    pos = (pos + steps) % i
    # buf = buf[:pos + 1] + [i] + buf[pos + 1:]
    if pos + 1 == 1:
        last_at_1 = i
    pos += 1
    if pos > i:
        pos -= i + 1

print(last_at_1)
