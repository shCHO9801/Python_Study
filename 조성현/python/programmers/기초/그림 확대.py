def solution(picture, k):
    answer = []
    for i in picture:
        tmp = ''
        for j in i:
            for l in range(k):
                tmp+=j
        for j in range(k):
            answer.append(tmp)
    return answer