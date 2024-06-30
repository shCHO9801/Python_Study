str = input()
l = 0
r = len(str)-1
answer = 1
while l<r:
    if str[l]==str[r]:
        l += 1
        r -= 1
    else:
        answer = 0
        break
print(answer)