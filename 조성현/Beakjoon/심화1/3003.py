p = [1,1,2,2,2,8]
arr = list(map(int,input().split()))
answer=0
for i in range(len(arr)):
    arr[i] = p[i] - arr[i]

for i in arr:
    print(i, end=' ')