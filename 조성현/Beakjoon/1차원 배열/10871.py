n,x = map(int,input().split())
arr = list(map(int, input().split()))
answer = [j for j in arr if j < x]
for i in answer:
    print(i, end=' ')