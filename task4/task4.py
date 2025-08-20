import sys


path1 = sys.argv[1]

with open(path1, encoding="UTF-8") as file_in:
    nums = file_in.read().strip().split('\n')

nums = [int(line) for line in nums]

max_steps = 20

mean = 0
lesser_m = -1

for i in nums:
    mean += i

mean /= len(nums)
sorted_num = sorted(nums, reverse=True)
absolute = 10000000000000000000000000000000000000000000000000000

for i in sorted_num:
    if abs(mean - i) < absolute or lesser_m == -1:
        absolute = abs(mean - i)
        lesser_m = i

mean = lesser_m

for i in range(len(nums)):
    while nums[i] != mean and max_steps != 0:
        max_steps -= 1
        if nums[i] > mean:
            nums[i] -= 1
        elif nums[i] < mean:
            nums[i] += 1

if max_steps != 0:
    print(20 - max_steps)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

