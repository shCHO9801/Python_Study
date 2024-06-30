def solution(numlist, n):
    answer = []
    for i in range(len(numlist) - 1):
        for j in range(len(numlist) - 1):
            if abs(n - numlist[j]) >= abs(n - numlist[j + 1]):
                if abs(n - numlist[j]) == abs(n - numlist[j + 1]):
                    if numlist[j] < numlist[j + 1]:
                        tmp = numlist[j]
                        numlist[j] = numlist[j + 1]
                        numlist[j + 1] = tmp
                else:
                    tmp = numlist[j]
                    numlist[j] = numlist[j + 1]
                    numlist[j + 1] = tmp

    return numlist