def solution(arr, queries):
    for q in queries:
        i,j = q
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    return arr