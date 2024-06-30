def solution(my_string, queries):
    my_string = list(my_string)
    for i in queries:
        s,e = i
        tmp = ''.join(my_string[j] for j in range(e,s-1,-1))
        idx = 0
        for j in range(s,e+1):
            my_string[j] = tmp[idx]
            idx+=1
    return ''.join(i for i in my_string)