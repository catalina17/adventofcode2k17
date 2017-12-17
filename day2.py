f = open("day2.txt", "r")

checksum = 0

res = 0
for line in f.readlines():
    nums = line.split()

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i != j:
                if int(nums[i]) % int(nums[j]) == 0:
                    res += int(nums[i]) / int(nums[j])

print(res)
