def solution(s):
    answer = []
    sle = len(s)
    count = 0
    zero = 0
    while len(s) != 1:
        zero += len([i for i in s if i== '0'])
        s = ''.join([i for i in s if i != '0'])
        sle = len(s)
        count += 1
        s = bin(sle)[2:]
    answer.extend([count, zero])
    return answer