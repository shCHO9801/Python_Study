def solution(quiz):
    answer = []
    for i in quiz:
        i += ' '
        tmp = []
        tmps = ''
        cur = ''
        for j in i:
            if j == ' ':
                if tmps in '+-=':
                    cur += tmps
                else:
                    tmp.append(int(tmps))
                tmps = ''
            else:
                tmps += j
        if '+' in cur:
            if tmp[0] + tmp[1] == tmp[2]:
                answer.append('O')
            else:
                answer.append('X')
        else:
            if tmp[0] - tmp[1] == tmp[2]:
                answer.append('O')
            else:
                answer.append('X')

    return answer