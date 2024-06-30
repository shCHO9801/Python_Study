def solution(emergency):
    tmp = [i for i in emergency]
    tmp.sort(reverse = True)
    return [tmp.index(i)+1 for i in emergency]