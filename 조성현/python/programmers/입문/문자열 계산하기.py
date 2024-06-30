def solution(my_string):
    num = []
    my_string += ' '
    calcul = ''
    tmp = ''
    for i in my_string:
        if i == ' ':
            if tmp == '+' or tmp =='-':
                calcul += tmp
            else:
                num.append(int(tmp))
            tmp = ''
        else:
            tmp+=i
    answer = num[0]
    idx = 1
    for i in calcul:
        if i == '+':
            answer+=num[idx]
        else:
            answer-=num[idx]
        idx+=1
    return answer