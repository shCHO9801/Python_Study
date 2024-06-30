def solution(str_list):
    answer = []
    idx = -1
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return answer
        elif str_list[i] == 'r':
            idx = i + 1
            break
        else:
            answer.append(str_list[i])

    if 'l' not in str_list and 'r' not in str_list:
        return []
    if idx != -1:
        return str_list[idx:]
    return answer