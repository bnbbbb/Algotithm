def solution(emergency):
    a = {j: i for i, j in enumerate(sorted(emergency, reverse=True), 1)}
    
    return [a[i] for i in emergency]