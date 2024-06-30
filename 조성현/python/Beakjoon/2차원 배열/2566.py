arr = []
max_i = 0
max_v = 0
max_j = 0
for i in range(9):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if max_v < max(temp):
        max_v = max(temp)
        max_i = i

for i in range(len(arr[max_i])):
    if arr[max_i][i] == max_v:
        max_j = i
        break

print(max_v)
print(max_i+1, max_j+1)