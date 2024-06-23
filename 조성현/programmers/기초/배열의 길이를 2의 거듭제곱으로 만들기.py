def solution(arr):
    num = 1
    while num < len(arr):
        num*=2
    while len(arr) < num:
        arr.append(0)
    return arr