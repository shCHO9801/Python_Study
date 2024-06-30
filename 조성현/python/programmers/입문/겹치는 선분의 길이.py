def solution(lines):
    answer = 0
    temp = [0 for i in range(202)]
    for i in lines:
        for j in range(i[0]+100,i[1]+100):
            temp[j]+=1
    for i in temp:
        if i>1:
            answer+=1
    return answer