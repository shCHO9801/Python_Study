def solution(n, k):
    answer = 12000 * n
    k-=n//10
    return answer + k * 2000