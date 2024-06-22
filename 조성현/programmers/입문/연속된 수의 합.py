def solution(num, total):
    answer = [i for i in range(1,num+1)]
    while(sum(answer)!=total):
        if sum(answer)<total:
            for i in range(0,num):
                answer[i]+=1
        else:
            for i in range(0,num):
                answer[i]-=1
    return answer