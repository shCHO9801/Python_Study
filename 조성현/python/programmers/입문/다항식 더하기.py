def solution(strc):
    answer = ''
    strc+=' '
    x = 0
    num = 0
    tmp = ''
    for i in strc:
        if i == '+':
            continue
        if i == ' ':
            if 'x' in tmp:
                if len(tmp) == 1:
                    x+=1
                else:
                    tmp2 = ''.join(j for j in tmp if j != 'x')
                    x+=int(tmp2)
            elif tmp!='':
                num+=int(tmp)
            tmp = ''
        else:
            tmp+=i
    if x!=0:
        if x==1:
            answer+='x'
        else:
            answer+=str(x)+'x'
        if num!=0:
            answer+=' + '
    if num!=0:
        answer+=str(num)
    return answer