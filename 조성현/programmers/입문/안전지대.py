def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(i-1,i+2):
                    if k<0 or k>len(board)-1:
                        continue
                    for l in range(j-1,j+2):
                        if l<0 or l>len(board[i])-1:
                            continue
                        if board[k][l] == 2 or board[k][l] == 1:
                            continue
                        board[k][l] = 2
    for i in board:
        for j in i:
            if j == 0:
                answer+=1
    return answer