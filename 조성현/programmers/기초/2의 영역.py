def solution(arr):
    answer = []
    sig = 0
    for i in arr:
        if i == 2:
            sig+=1
        if sig > 0:
            answer.append(i)
    if sig == 0:
        return [-1]
    if sig == 1:
        return [2]
    while answer[-1] != 2:
        answer.pop()
    return answer