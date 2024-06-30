def solution(my_string):
    answer = 0
    tmp = []
    tmp_s = ''
    my_string += 'a'
    for i in my_string:
        if i not in '1234567890':
            if tmp_s != '':
                tmp.append(int(tmp_s))
                tmp_s = ''
            continue
        else:
            tmp_s += i

    return sum(tmp)

