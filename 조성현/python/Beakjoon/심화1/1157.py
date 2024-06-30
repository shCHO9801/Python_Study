str = input()
str = str.upper()
alpha = [0 for i in range(26)]
for i in str:
    alpha[ord(i)-ord('A')] += 1
max_val = max(alpha)
cnt = 0
result = 0
for i in range(26):
    if alpha[i] == max_val:
        cnt += 1
        result = i
if cnt >1:
    print('?')
else:
    print(chr(ord('A') + result))