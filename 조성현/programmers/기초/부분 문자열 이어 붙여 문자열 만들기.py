def solution(my_strings, parts):
    answer = ''
    idx = 0
    for i in parts:
        answer+=my_strings[idx][i[0]: i[1]+1]
        idx+=1
    return answer