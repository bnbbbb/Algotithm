def solution(X, Y):
    answer = []
    Z = set(X)
    for j in Z:
        if j in Y:
            answer+=j * min(Y.count(j), X.count(j))
    answer.sort(reverse = True)
    if answer == []:
        return '-1'
    elif all(element == '0' for element in answer):
        return '0'
    return ''.join(answer)