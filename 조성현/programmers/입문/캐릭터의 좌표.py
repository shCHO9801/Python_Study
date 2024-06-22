def solution(keyinput, board):
    answer = [0,0]
    x_max = board[0]//2
    y_max = board[1]//2
    for i in keyinput:
        if i == 'left':
            if answer[0] > x_max*-1:
                answer[0]-=1
        if i == 'right':
            if answer[0] < x_max:
                answer[0]+=1
        if i == 'up':
            if answer[1] < y_max:
                answer[1]+=1
        if i == 'down':
            if answer[1] > y_max*-1:
                answer[1]-=1
    return answer