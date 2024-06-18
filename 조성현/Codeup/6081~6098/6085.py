w,h,b = map(int,input().split())
answer = float(w*h*b/8)
answer = answer/1024/1024
print(format(answer, '.2f'),'MB')