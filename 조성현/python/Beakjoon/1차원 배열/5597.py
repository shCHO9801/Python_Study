arr = [0 for i in range(31)]
for i in range(28):
    x = int(input())
    arr[x] = 1
for i in range(1,31):
    if arr[i] != 1:
        print(i)