cnt = 0
str = input()
for i in str:
    if i == ' ':
        cnt += 1
if str[-1] != ' ':
    cnt += 1
if str[0] == ' ':
    cnt -= 1
print(cnt)