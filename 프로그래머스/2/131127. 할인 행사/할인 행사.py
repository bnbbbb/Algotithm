from collections import Counter

def solution(want, number, discount):
    answer = 0
    a = dict(zip(want, number))
    
    for i in range(len(discount)):
        result = Counter(discount[i:i+10])
        if all(result.get(j, 0) >= x for j, x in a.items()):
            answer += 1  
    return answer