arr = [0 for i in range(42)]
cnt = 0

for i in range(10):
    x = int(input())
    arr[x%42] += 1
for i in range(42):
    if arr[i] > 0:
        cnt+=1
print(cnt)