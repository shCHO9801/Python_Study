arr = []
for i in range(19):
    arr.append([])
    x = input().split()
    for j in range(len(x)):
        arr[i].append(int(x[j]))


n = int(input())
for i in range(n):
    x,y=input().split()
    x = int(x)-1
    y = int(y)-1
    for j in range(19):
        if arr[x][j] == 0:
            arr[x][j] = 1
        else:
            arr[x][j] = 0
    for j in range(19):
        if arr[j][y] == 0:
            arr[j][y] = 1
        else:
            arr[j][y] = 0


for i in arr:
    for j in i:
        print(j, end=' ')
    print()