def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        tmp = my_string[i:]
        answer.append(tmp)
    return sorted(answer)