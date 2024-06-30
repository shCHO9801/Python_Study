def solution(ineq, eq, n, m):
    ineq+=eq
    if ineq == '>=':
        return 1 if n>=m else 0
    if ineq == '<=':
        return 1 if n<=m else 0
    if ineq == '>!':
        return 1 if n>m else 0
    return 1 if n<m else 0