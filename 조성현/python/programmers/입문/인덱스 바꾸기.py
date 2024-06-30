def solution(strg, num1, num2):
    strg = list(strg)
    tmp = strg[num1]
    strg[num1] = strg[num2]
    strg[num2] = tmp
    return ''.join(i for i in strg)