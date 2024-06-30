def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list)-n+1,n):
        tmp = [num_list[j] for j in range(i,i+n)]
        answer.append(tmp)
    return answer