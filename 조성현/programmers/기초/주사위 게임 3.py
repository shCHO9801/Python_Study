def solution(a, b, c, d):
    dice = [a,b,c,d]
    dice.sort()
    if dice[0] == dice[1] == dice[2] == dice[3]:
        return 1111*dice[0]
    elif dice[0] == dice[1] == dice[2]:
        return (dice[1]*10 + dice[3])**2
    elif dice[1] == dice[2] == dice[3]:
        return (dice[1]*10 + dice[0])**2
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0]+dice[2])*abs(dice[0]-dice[2])
    elif dice[0] == dice[1]:
        return dice[2]*dice[3]
    elif dice[1] == dice[2]:
        return dice[0]*dice[3]
    elif dice[3] == dice[2]:
        return dice[0]*dice[1]
    return dice[0]