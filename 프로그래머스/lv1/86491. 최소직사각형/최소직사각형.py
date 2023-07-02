import itertools

def solution(sizes):
    answer = []
    mv = max(list(itertools.chain(*sizes)) )
    for i in sizes:
        a, b = max(i), min(i)
        answer.append(b)
    
    
    return mv * max(answer)