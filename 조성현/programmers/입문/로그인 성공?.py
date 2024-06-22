def solution(id_pw, db):
    sig = ['login', 'wrong pw', 'fail']
    sign = 2
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return sig[0]
            else:
                sign = 1
    return sig[sign]