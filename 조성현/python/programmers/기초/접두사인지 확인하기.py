def solution(my_string, is_prefix):
    tmp = ''
    for i in my_string:
        if is_prefix == tmp:
            return 1
        tmp+=i
    return 0