from itertools import product

def solution(n, info):
    info.reverse()
    result = [-1]
    maxd = 0
    a= list(product((True, False), repeat=11))
    for win in product((True, False), repeat=11):
        t = 0
        s = sum(info[j]+1 for j in range(11) if win[j])
        if s <= n:
            apeach = sum(j for j in range(11) if not win[j] and info[j])
            ryan = sum(j for j in range(11) if win[j])
            d = ryan - apeach
            if d > maxd:
                maxd = d
                result = [info[j]+1 if win[j] else 0 for j in range(11)]
                result[0] += n - s
    result.reverse()
    return result