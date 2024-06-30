board = []
for i in range(20):
    board.append([0 for j in range(20)])

for i in range(20):
    board.append(0)
for i in range(1,20):
        x = map(int, input().split())
        for j in range(20):
            board[i][j] = x[j]
        board[i].append(x)

# n = int(input())
# for i in range(n):
#     x,y = map(int,input().split())
#     for j in range(1,20):
#         if board[x][j]==1:
#             board[x][j]=0
#         else:
#             board[x][j]=1
#         if board[j][y]==1:
#             board[j][y]=0
#         else:
#             board[j][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(board[i][j],end=" ")
    print()