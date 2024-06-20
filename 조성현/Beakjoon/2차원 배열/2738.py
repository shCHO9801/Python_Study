y,x = map(int,input().split())
A = []
B = []
for i in range(y):
    tmp = list(map(int,input().split()))
    A.append(tmp)
for i in range(y):
    tmp = list(map(int,input().split()))
    B.append(tmp)
# for i in range(2):

for i in range(y):
    for j in range(x):
        A[i][j]+=B[i][j]

for i in A:
    for j in i:
        print(j,end=" ")
    print()