def solution(babbling):
    answer = 0
    babb = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        tmp = ''
        saied = []
        i+=' '
        for j in i:
            tmp+=j
            if j==' ':
                if tmp == ' ':
                    answer+=1
                    break
            elif tmp in babb:
                if tmp not in saied:
                    saied.append(tmp)
                else:
                    break
                tmp = ''
    return answer