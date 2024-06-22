def solution(array):
    answer = 0
    count = [0 for i in range(1001)]
    for i in array:
        count[i] += 1
    max_count = max(count)
    cnt = 0
    for i in range(0, 1001):
        if count[i] == max_count:
            cnt += 1
    if cnt >= 2:
        return -1

    return count.index(max_count)