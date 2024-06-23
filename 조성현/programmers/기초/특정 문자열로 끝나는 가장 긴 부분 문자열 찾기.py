def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        tmp = myString[:len(myString) - i]
        tmp2 = tmp[len(tmp) - len(pat):]
        if tmp2 == pat:
            return tmp

    return answer