n = int(input())
for i in range(n):
    a, str = input().split()
    a = int(a)
    for j in str:
        print(j*a,end='')
    print()