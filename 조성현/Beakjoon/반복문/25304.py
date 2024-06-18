x = int(input())
n = int(input())
result = 0
for i in range(n):
    price,num = map(int,input().split())
    result += price*num
if result == x:
    print('Yes')
else:
    print('No')