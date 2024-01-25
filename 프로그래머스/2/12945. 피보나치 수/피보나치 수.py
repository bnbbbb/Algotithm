def solution(n):
    prev, next = 0, 1
    
    for _ in range(n-1):
        prev , next = next, prev + next
        
    return next % 1234567