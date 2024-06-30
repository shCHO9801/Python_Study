def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat)+1):
        tmp = myString[i:i+len(pat)]
        if tmp == pat:
            answer+=1
    return answer