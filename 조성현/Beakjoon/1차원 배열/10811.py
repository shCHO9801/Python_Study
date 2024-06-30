n,m = map(int,input().split())
arr = [i for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    tmp = [arr[j] for j in range(b,a-1,-1)]
    k=0
    for j in range(a,b+1):
        arr[j] = tmp[k]
        k+=1

for i in range(1, n+1):
    print(arr[i], end=' ')