def solution(quiz):
    answer = []
    a = []
    for i in quiz:
        a.append(i.split(' '))
    for i in a:
        op1, op2, op3, op4, op5 = i
        if op2 == '+':
            if int(op1) + int(op3) == int(op5):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(op1) - int(op3) == int(op5):
                answer.append('O')
            else:
                answer.append('X')
    return answer