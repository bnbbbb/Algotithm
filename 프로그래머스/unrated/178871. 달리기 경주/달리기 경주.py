def solution(players, callings):
    rank = {j: i for i, j in  enumerate(players)}
    rev = {i: j for i, j in  enumerate(players)}
    for i in callings:
        ran = rank[i]
        name =  rev[ran-1]
        
        rank[i] -= 1
        rank[name] += 1
        
        rev[ran] = name
        rev[ran-1] = i
    answer = dict(sorted(rank.items(), key= lambda x: x[1]))
    answer = [key for key, _ in answer.items()]
    return answer