def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = 0 if mode == 1 else 1
        elif mode == 0:
            if i%2==0:
                answer+=code[i]
        else:
            if i%2==1:
                answer+=code[i]
    if answer == '':
        return 'EMPTY'
    return answer