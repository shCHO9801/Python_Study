import math
def solution(n):
    tmp = math.sqrt(n)
    for i in range(1,int(tmp)+1):
        if i*i == n:
            return 1
    return 2