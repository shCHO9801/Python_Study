def solution(my_string, indices):
    my_string = list(my_string)
    return ''.join(my_string[i] for i in range(len(my_string))if i not in indices)