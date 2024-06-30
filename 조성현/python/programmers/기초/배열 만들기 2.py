def solution(l, r):
    answer = []
    for i in range(l,r+1):
        tmp = ''
        for j in str(i):
            if j not in tmp:
                tmp+=j
        if tmp =='5' or tmp == '0' or tmp == '50':
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer