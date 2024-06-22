def solution(numbers):
    numbers += ' '
    answer_str = ''
    str_a = {"zero": "0", "one": "1", "two": "2", "three": "3",
             "four": "4", "five": '5', "six": '6', "seven": "7", "eight": "8", "nine": "9"}
    tmp = ''
    for i in numbers:
        if tmp in str_a:
            answer_str += str_a[tmp]
            tmp = ''
        tmp += i

    return int(answer_str)