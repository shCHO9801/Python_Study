def solution(a, d, included):
    answer = 0
    tmp = [a]
    for i in range(len(included)):
        tmp.append(tmp[-1] + d)
    for i in range(len(included)):
        if included[i]:
            answer += tmp[i]

    return answer