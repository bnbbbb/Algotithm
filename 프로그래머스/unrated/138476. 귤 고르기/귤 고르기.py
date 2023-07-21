from collections import Counter
def solution(k, tangerine):
    answer = []
    con = Counter(tangerine)
    con = sorted(con.items(), key=lambda x: x[1], reverse=True)
    for key, i in con:
        for j in range(i):
            answer.append(key)
        if len(answer) >= k:
                break
    return len(set(answer))