def solution(my_string):
    answer = [0 for i in range(52)]
    for i in my_string:
        if i.isupper():
            answer[ord(i)-ord('A')]+=1
        else:
            answer[ord(i)-ord('a')+26]+=1
    return answer