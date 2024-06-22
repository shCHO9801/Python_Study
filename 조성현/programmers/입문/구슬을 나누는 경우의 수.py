def solution(n, m):
    nf = 1
    for i in range (1,n+1):
        nf*=i
    nmm = 1
    mf = 1
    for i in range(1,n-m+1):
        nmm*=i
    for i in range(1,m+1):
        mf*=i
    nmm*=mf
    return nf/nmm