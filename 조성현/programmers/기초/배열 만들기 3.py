def solution(arr, intervals):
    answer = []
    for q in intervals:
        s,e = q
        for i in range(s,e+1):
            answer.append(arr[i])
    return answer