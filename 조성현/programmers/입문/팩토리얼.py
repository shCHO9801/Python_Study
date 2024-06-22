def solution(n):
    answer = 1
    fac = 1
    while True:
        fac *= answer
        answer += 1
        if fac > n:
            break

    return answer - 2