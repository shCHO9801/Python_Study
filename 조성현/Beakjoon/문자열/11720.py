n = int(input())
str = input()
answer = 0
for i in str:
    answer += ord(i)-ord('0')
print(answer)