def solution(n, words):
    
    stack = []
    
    for i in range(len(words)):
        if words[i] in stack:
            return [(i % n) +1, (i // n) + 1]
        if i > 0 and words[i][0] != words[i-1][-1]:
            return [(i % n) +1, (i // n) + 1]
        stack.append(words[i])
        
    return [0,0]