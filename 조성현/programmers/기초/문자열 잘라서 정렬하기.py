def solution(myString):
    tmp = sorted(myString.split('x'),reverse=True)
    while tmp[-1] == '':
        tmp.pop()
    return sorted(tmp)