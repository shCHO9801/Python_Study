arr = [0]
for i in range(9):
    arr.append(int(input()))
max_value = max(arr)
max_idx = 0
for i in range(10):
    if arr[i] == max_value:
        max_idx = i
        break
print(max_value)
print(max_idx)