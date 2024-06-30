n = int(input())
answer=0
for i in range(n):
    str = input()
    tmp = ''
    tmp += str[0]
    prev = str[0]
    flag = 1
    for j in str:
        if j == prev:
            continue
        else:
            if j in tmp:
                flag = 0
                break
            tmp += j
            prev = j
    answer += flag
print(answer)