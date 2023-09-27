from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    
    siso = [1/2, 2/3, 3/4]
    # answer =  len(weights) - len(set(weights))
    for k, v in count.items():
        print(v)
        if v > 1: answer += v * (v-1) / 2
    weights = list(set(weights))
    
    for w in weights:
        for s in siso:
            if w * s in weights:
                answer += count[w] * count[w*s]
    return answer    