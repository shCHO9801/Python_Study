a = input().split()
answer = 0
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
if a[0] == a[1] == a[2]:
    answer = 10000 +a[0]*1000
elif a[0] == a[1] or a[1] == a[2]:
    answer = 1000 + a[1] *100
else:
    answer = a[2]*100
print(answer)
