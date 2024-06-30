def solution(sides):
    answer = 0
    tmp = 1
    while min(sides) + max(sides) > tmp:
        if tmp + min(sides) > max(sides):
            answer+=1
        elif max(sides)<tmp and min(sides) + max(sides) > tmp:
            answer+=1
        tmp+=1
    return answer