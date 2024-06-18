a = int(input())
b = int(input())
c = b
b1 = b//100
b %= 100
b2 = b//10
b2 %= 10
b3 = b%10
print(a*b3)
print(a*b2)
print(a*b1)
print(a*c)