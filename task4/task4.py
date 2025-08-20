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

while max_steps != 0:
    max_steps -= 1
    num_of_same = 0
    for i in range(len(nums)):
        if nums[i] > mean:
            nums[i] -= 1
        elif nums[i] < mean:
            nums[i] += 1
        else:
            num_of_same += 1
    if num_of_same == len(nums):
        break

# print(nums)
if max_steps != 0:
    print(20 - max_steps)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

