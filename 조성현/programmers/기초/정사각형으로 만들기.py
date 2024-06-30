def solution(arr):
    size = len(arr)
    for i in arr:
        while len(i) < size:
            i.append(0)
    size = len(arr[0])
    while len(arr) < size:
        arr.append([0 for i in range(size)])
    return arr