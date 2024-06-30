def solution(myString):
    return ''.join('A' if i == 'a' or i == 'A' else i.lower() for i in myString)