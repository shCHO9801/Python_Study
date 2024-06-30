arr = []
cnt = 0
for i in range(101):
    temp = [0 for j in range(101)]
    arr.append(temp)

n=int(input())
for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            arr[j][k] = 1

for i in arr:
    for j in i:
        if j == 1:
            cnt+=1
print(cnt)