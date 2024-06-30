def solution(s):
    s+=' '
    answer = 0
    prev = 0
    tmp = ''
    for i in s:
        if i== 'Z':
            answer-=prev
            continue
        if i != ' ':
            tmp+=i
            continue
        if i==' ':
            if tmp !='':
                prev = int(tmp)
                answer+=prev
                tmp=''
    return answer