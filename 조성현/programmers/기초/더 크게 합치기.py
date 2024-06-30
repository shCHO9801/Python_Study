def solution(a, b):
    tmp1 = int(str(a)+str(b))
    tmp2 = int(str(b)+str(a))
    return tmp1 if tmp1 > tmp2 else tmp2