def solution(spell, dic):
    answer = 2
    for i in dic:
        flag = -1
        for j in spell:
            if j not in i:
                flag = 1
                break
        if flag == -1:
            answer = 1
    return answer