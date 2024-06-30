def solution(dots):
    maxx = dots[0][0]
    maxy = dots[0][1]
    minx = dots[0][0]
    miny = dots[0][1]
    for i in dots:
        if i[0] > maxx:
            maxx = i[0]
        if i[0] < minx:
            minx = i[0]
        if i[1] > maxy:
            maxy = i[1]
        if i[1] < miny:
            miny = i[1]
    return (maxx-minx) * (maxy-miny)