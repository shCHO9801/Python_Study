def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    idx = s
    for i in overwrite_string:
        my_string[idx] = i
        idx+=1
    return ''.join(i for i in my_string)