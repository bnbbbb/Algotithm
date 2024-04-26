from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    smbro = set()
    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            del bro[i]
        smbro.add(i)
        if len(bro) == len(smbro):
            answer += 1
            
    return answer