def solution(array):
    temp = ''.join(str(i) for i in array)
    return len([i for i in temp if i == '7'])