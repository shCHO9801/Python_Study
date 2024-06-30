def solution(my_str, n):
    answer = []
    tmp = ''
    for i in my_str:
        if len(tmp) >= n:
            answer.append(tmp)
            tmp = ''
        tmp += i
    if tmp != '':
        answer.append(tmp)
    return answer