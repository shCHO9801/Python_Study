def solution(A, B):
    if A == B:
        return 0
    temp_list = []
    temp_list.append(A)
    for j in range(len(A) - 1):
        TA = list(A)
        tmp = TA[-1]
        for i in range(0, len(A) - 1):
            tmp += TA[i]
        temp_list.append(tmp)
        A = tmp

    if B in temp_list:
        return (temp_list.index(B))
    return -1