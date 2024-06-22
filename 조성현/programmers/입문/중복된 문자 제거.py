def solution(my_string):
    tmp=''
    answer = ''
    for i in my_string:
        if i not in tmp:
            answer+=i
            tmp+=i
    return answer