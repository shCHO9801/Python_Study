def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                if len(answer) != 0:
                    answer.pop()
    return answer