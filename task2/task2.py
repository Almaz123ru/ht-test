import sys


path1 = sys.argv[1]
path2 = sys.argv[2]

with open(path1, encoding="UTF-8") as file_in:
    circle_file = file_in.read().strip().split('\n')

with open(path2, encoding="UTF-8") as file_in:
    dots_file = file_in.read().strip().split('\n')

circle_center = list(map(float, circle_file[0].split(' ')[0:2]))
circle_radius = list(map(float, circle_file[1].split(' ')[0:2]))

dots = [list(map(float, line.split())) for line in dots_file]


for line in dots:
    value = (((line[0] - circle_center[0]) ** 2) / (circle_radius[0] ** 2) +
             ((line[1] - circle_center[1]) ** 2) / (circle_radius[1] ** 2))
    if value == 1:
        print(0)
    elif value < 1:
        print(1)
    else:
        print(2)

