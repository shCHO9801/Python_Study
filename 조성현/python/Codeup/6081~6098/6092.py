n = int(input())
arr = [0 for i in range(24)]
a = map(int, input().split())
for i in a:
    arr[i] += 1
for i in range(1,24):
    print(arr[i], end=' ')

