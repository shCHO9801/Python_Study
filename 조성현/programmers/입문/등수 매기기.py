def solution(score):
    temp = []
    for i in score:
        temp.append(i[0]+i[1])
    temp.sort(reverse = True)
    return [temp.index(i[0] + i[1])+1 for i in score]