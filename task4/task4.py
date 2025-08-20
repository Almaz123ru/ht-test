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

for i in nums:
    if abs(mean - i) < abs(lesser_m - i) or lesser_m == -1:
        lesser_m = i

mean = lesser_m

for i in range(len(nums)):
    while nums[i] != mean and max_steps != 0:
        max_steps -= 1
        if nums[i] > mean:
            print(max_steps, "   -   ")
            nums[i] -= 1
            # break
        elif nums[i] < mean:
            print(max_steps, "   +   ")
            nums[i] += 1
            # break
        print(max_steps)

print(nums)
if max_steps != 0:
    print(20 - max_steps)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

