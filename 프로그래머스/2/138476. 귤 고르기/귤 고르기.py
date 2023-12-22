from collections import Counter
def solution(k, tangerine):
    answer = 0
    con = Counter(tangerine)
    con = sorted(con.items(), key=lambda x: x[1], reverse=True)
    
    for _, i in con:
        k -= i
        answer+=1
        if k <= 0:
            break
    return answer