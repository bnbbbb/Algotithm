from itertools import product
def solution(word):
    answer = 0
    result = []
    words = ['A', 'E','I','O','U']
    for i in range(1, 6):
        for j in product(words, repeat=i):
            result.append(j)
    result.sort()
    for idx, value in enumerate(result):
        ans = ''.join(value)
        if word == ans:
            answer = idx + 1
    return answer