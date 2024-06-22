def solution(i, j, k):
    answer = 0
    for l in range(i, j + 1):
        for a in str(l):
            if a == str(k):
                answer += 1

    return answer