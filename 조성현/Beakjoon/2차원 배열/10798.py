arr = []
max_len = 0
idx = 0
for i in range (5):
    temp = input()
    arr.append(temp)
    if len(temp) > max_len:
        max_len = len(temp)

while idx < max_len:
    for i in range(5):
        if len(arr[i])-1 < idx:
            continue
        print(arr[i][idx],end='')
    idx+=1