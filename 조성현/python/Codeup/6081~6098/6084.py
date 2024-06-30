h,b,c,s = map(int, input().split())
answer = float(h*b*c*s/8)
answer = answer/1024/1024
print(format(answer,'.1f'),'MB')