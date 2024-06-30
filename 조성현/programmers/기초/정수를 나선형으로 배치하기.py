def solution(n):
    arr = [[0 for i in range(n)] for j in range(n)]

    si = 0
    sj = 0
    ei = n-1
    ej = n-1
    idx = 1
    while True:
        for j in range(sj,ej+1):
            arr[si][j] = idx
            idx += 1
        si+=1
        if idx > n*n:
            break
        for i in range(si,ei+1):
            arr[i][ej] = idx
            idx+=1
        ej-=1
        if idx > n*n:
            break
        for j in range(ej,sj-1,-1):
            arr[ei][j] = idx
            idx+=1
        ei-=1
        if idx > n*n:
            break
        for i in range(ei,si-1,-1):
            arr[i][sj] = idx
            idx+=1
        sj+=1
        if idx > n*n:
            break


    return arr