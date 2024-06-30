board = []
for i in range(10):
    board.append([])
    for j in range(10):
        board[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        board[i][j] = int(a[j])

i = 1
j = 1
while True:
    if i>8 or j>8:
        break
    if board[i][j] == 2:
        board[i][j] = 9
        break
    board[i][j] = 9
    if board[i][j+1] == 1:
        i+=1
    else:
        j+=1


for i in board:
    for j in i:
        print(j, end=' ')
    print()