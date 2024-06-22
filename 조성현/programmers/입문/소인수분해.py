def solution(n):
    answer = []
    idx = 2
    while idx<=n:
        while n%idx==0:
            if idx not in answer:
                answer.append(idx)
            n/=idx
        idx+=1
    return answer