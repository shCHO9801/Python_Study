a = int(input())
cnt = 1
sum = 0
while True:
    sum += cnt
    cnt += 1
    if sum >= a:
        break
print(sum)