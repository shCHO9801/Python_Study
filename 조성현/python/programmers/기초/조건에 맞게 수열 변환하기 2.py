def solution(arr):
    answer = -1
    tmp = []
    while tmp != arr:
        answer+=1
        tmp = [i for i in arr]
        for i in range(len(arr)):
            if arr[i] >=50 and arr[i]%2==0:
                arr[i]//=2
            elif arr[i] < 50 and arr[i]%2==1:
                arr[i] = arr[i]*2+1
    return answer