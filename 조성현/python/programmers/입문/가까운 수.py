def solution(array, n):
    array.sort()
    cur = array[0]
    cur_check = 101
    if cur_check < 0:
        cur_chek *= -1
    for i in array:
        temp = i-n
        if temp < 0:
            temp *= -1
        if temp < cur_check:
            cur_check = temp
            cur = i
    return cur
