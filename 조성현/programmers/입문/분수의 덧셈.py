def solution(numer1, denom1, numer2, denom2):
    bj = numer1 * denom2 + numer2 * denom1
    bm = denom2 * denom1
    idx = 2
    while idx < bm or idx < bj:
        while bj % idx == 0 and bm % idx == 0:
            bj//=idx
            bm//=idx
        idx+=1
    return [bj,bm]