arr = [-1 for i in range(26)]
str = input()
for i in range(len(str)):
    x = ord(str[i])-ord('a')
    if arr[x] == -1:
        arr[x] = i
for i in arr:
    print(i,end=' ')