import sys

def rank_sort(ranks, np, p):
    if ranks and ranks[-1] >= np and len(ranks) == p:
        return False
    else:
        ranks.append(np)
        ranks.sort(reverse=True)
    return ranks[:p]

def re_rank(ranks, np, p):
    ranks = rank_sort(ranks, np, p)

    if not ranks:
        return False
    count = 1
    rank = 1
    rank_dict = {ranks[0] : 1}
    for i in range(1, len(ranks)):
        if ranks[i-1] == ranks[i]:
            rank_dict[ranks[i]] = rank
            count += 1
        else:
            rank += count
            rank_dict[ranks[i]] = rank
            count = 1
    return rank_dict
n, np, p = map(int, sys.stdin.readline().split())

ranks = list(map(int, sys.stdin.readline().split()))
if not ranks:
    ranks = []
    
result = re_rank(ranks, np, p)
print(result[np] if result else -1)