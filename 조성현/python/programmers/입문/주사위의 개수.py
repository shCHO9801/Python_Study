def solution(box, n):
    answer = 1
    tmp = [i//n for i in box]
    for i in tmp:
        answer *= i
    return answer