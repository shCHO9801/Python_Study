n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
for i in range(len(arr)):
    arr[i] = arr[i]/max_value*100
print(sum(arr)/n)