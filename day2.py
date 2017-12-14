f = open("day2.txt", "r")

checksum = 0

for line in f.readlines():
    nums = line.split()
    min_val = 1<<32
    max_val = -1<<32

    for num in nums:
        min_val = min(min_val, int(num))
        max_val = max(max_val, int(num))

    checksum += max_val - min_val

print(checksum)
