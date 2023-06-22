def solution(order):
    answer = 0
    return sum([4500 if 'americano' in i else 5000 if 'latte' in i else 4500 for i in order ] )