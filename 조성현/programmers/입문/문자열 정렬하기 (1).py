def solution(my_string):
    answer = [int(i) for i in my_string if i in '1234567890']
    return sorted(answer)