def solution(age):
    alpha = 'abcdefghijklmnopqrstuv'
    return ''.join(alpha[int(i)] for i in str(age))