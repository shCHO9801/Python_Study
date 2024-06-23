def solution(n_str):
    idx = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            idx = i
            break
    return ''.join(n_str[i] for i in range(idx,len(n_str)))