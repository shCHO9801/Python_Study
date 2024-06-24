def solution(n, m, section):
    answer = 0
    arr = [1]*(n+1)
    arr[0] = 1
    start = min(section)
    end = max(section)
    for i in section:
        arr[i] = 0
    idx = start
    while idx <= end:
        if arr[idx] == 0:
            answer+=1
            idx+=m
        else:
            idx+=1
    
            
    return answer
