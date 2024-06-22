def solution(chicken):
    answer = 0
    cou = chicken
    while cou >= 10:
        answer += cou//10
        cou = cou%10 + cou//10
    return answer