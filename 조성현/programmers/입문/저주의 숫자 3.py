def solution(n):
    idx = 1
    num = 1
    while idx < n:
        num+=1
        idx+=1
        while num%3==0 or '3' in str(num):
            num+=1
    return num