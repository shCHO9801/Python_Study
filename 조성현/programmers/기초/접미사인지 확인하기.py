def solution(my_string, is_suffix):
    for i in range(len(my_string)-1,-1,-1):
        if my_string[i:] == is_suffix:
            return 1
    return 0