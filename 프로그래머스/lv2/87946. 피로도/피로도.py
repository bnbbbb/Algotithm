from itertools import permutations
def solution(k, dungeons):
    answer = []
    result = 0
    ans = list(permutations(dungeons, len(dungeons)))
    a = k 
    
    for i in ans:
        a = k
        result = 0
        for j in i:
            if a >= j[0]:
                result+= 1
                a -= j[1]
        answer.append(result)
        
    return max(answer)