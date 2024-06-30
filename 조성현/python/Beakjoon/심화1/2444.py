n = int(input())
star = 1
space = n-1
for i in range(n*2-1):
    for j in range(space):
        print(' ',end='')
    for j in range(star):
        print('*',end='')
    if i<n-1:
        space-=1
        star+=2
    else:
        space+=1
        star-=2
    print()