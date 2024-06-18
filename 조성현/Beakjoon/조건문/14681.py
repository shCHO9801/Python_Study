a= int(input())
b= int(input())
answer=0
if a>0:
    if b>0:
        answer=1
    else:
        answer=4
else:
    if b>0:
        answer=2
    else:
        answer=3
print(answer)