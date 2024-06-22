def solution(numbers, direction):
    if direction == 'right':
        tmp = [numbers[-1]]
        tmp += numbers[0:len(numbers)-1]
        return tmp
    else:
        tmp = numbers[1:]
        tmp.append(numbers[0])
        return tmp