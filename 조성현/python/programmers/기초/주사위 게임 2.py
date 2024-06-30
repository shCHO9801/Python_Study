def solution(a, b, c):
    d = [a,b,c]
    answer = (a**3+b**3+c**3) * (a**2+b**2+c**2) * (a+b+c)
    d.sort()
    if d[0] == d[1] == d[2]:
        return answer
    elif d[0] == d[1] or d[1] == d[2]:
        return (a**2+b**2+c**2) * (a+b+c)
    return (a+b+c)