def solution(myStr):
    answer = []
    myStr+='a'
    tmp = ''
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if tmp != '':
                answer.append(tmp)
                tmp = ''
        else:
            tmp+=i
    if len(answer) == 0:
        return ['EMPTY']
    return answer