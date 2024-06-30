def solution(arr, queries):
    answer = []
    for q in queries:
        s,e,k = q
        min_value = 1000001
        for i in range(s,e+1):
            if arr[i] > k:
                if min_value > arr[i]:
                    min_value = arr[i]
        if min_value == 1000001:
            answer.append(-1)
        else:
            answer.append(min_value)
    return answer