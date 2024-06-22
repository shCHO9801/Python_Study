def solution(my_string):
    my_string = my_string.lower()
    return ''.join(i for i in sorted(my_string))