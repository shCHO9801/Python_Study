def solution(order):
    answer = 0
    for i in str(order):
        num = int(i)
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            answer += 1
    return answer