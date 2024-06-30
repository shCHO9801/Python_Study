w,h = map(int,input().split())
n = int(input())
arr = []

for i in range(w):
    arr.append([])
    for j in range(h):
        arr[i].append(0)

for i in range(n):
    l,d,x,y = map(int,input().split())
    x-=1
    y-=1
    if d==1:
        for j in range(l):
            arr[x+j][y] = 1
    else:
        for j in range(l):
            arr[x][y+j] = 1


for i in arr:
    for j in i:
        print(j,end=" ")
    print()