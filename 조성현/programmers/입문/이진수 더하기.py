def solution(bin1, bin2):
    if bin1 == '0' and bin2 == '0':
        return '0'
    answer = ''
    list_bin1 = [int(bin1[i]) for i in range(len(bin1) - 1, -1, -1)]
    list_bin2 = [int(bin2[i]) for i in range(len(bin2) - 1, -1, -1)]
    for i in range(10 - len(bin1) + 1):
        list_bin1.append(0)
    for i in range(10 - len(bin2) + 1):
        list_bin2.append(0)
    tmp = [list_bin1[i] + list_bin2[i] for i in range(0, 11)]
    cur = 0
    for i in range(0, 11):
        tmp[i] += cur
        if tmp[i] > 1:
            tmp[i] -= 2
            cur = 1
        else:
            cur = 0
    if cur == 1:
        tmp += '1'
    tmp = tmp[::-1]
    flg = -1
    for i in tmp:
        if flg == -1:
            if i == 1:
                flg = 1
        if flg == 1:
            answer += str(i)

    return answer