a,b,c = map(int,input().split())
tmp = a
if a>b:
    tmp = b
if tmp>c:
    tmp = c
print(tmp)
