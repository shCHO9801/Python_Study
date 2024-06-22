def solution(numbers):
    tmp = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j:
                continue
            tmp.append(numbers[i]*numbers[j])
    return max(tmp)