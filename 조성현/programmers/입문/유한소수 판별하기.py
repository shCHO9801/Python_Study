def solution(a, b):
    answer = 0
    idx = 2
    while idx < b:
        while a%idx==0 and b%idx==0:
            a//=idx
            b//=idx
        idx+=1
    if b==1:
        return 1
    idx = 2
    tmp = ''
    while idx <= b:
        while b%idx == 0:
            if str(idx) not in tmp:
                tmp+=str(idx)
            b//=idx
        idx+=1
    if tmp in ['2','5','25']:
        return 1
    return 2