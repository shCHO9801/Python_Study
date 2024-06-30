def solution(s):
    answer = ''
    count = [0 for i in range(26)]
    for i in s:
        tmp = ord(i)-ord('a')
        count[tmp]+=1
    for i in range(26):
        if count[i]== 1:
            answer+=chr(i+ord('a'))
    return answer