def solution(rank, attendance):
    answer = 0
    tmp = [rank[i] for i in range(len(rank)) if attendance[i]]
    tmp.sort()
    return rank.index(tmp[0])*10000 + rank.index(tmp[1]) * 100 + rank.index(tmp[2])