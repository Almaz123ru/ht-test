import sys


n1 = int(sys.argv[1])
m1 = int(sys.argv[2])

n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

arr = []
path = ''
for i in range(1, n1+1):
    arr.append(i)

last_in = 0
path = path + str(arr[last_in])
while True:
    last_in += m1 - 1
    if last_in >= n1:
        last_in -= n1
    if last_in == 0:
        break
    path = path + str(arr[last_in])

arr = []
for i in range(1, n2+1):
    arr.append(i)

last_in = 0
path = path + str(arr[last_in])
while True:
    last_in += m2 - 1
    if last_in >= n2:
        last_in -= n2
    if last_in == 0:
        break
    path = path + str(arr[last_in])

print(path)
