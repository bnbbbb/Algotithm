def solution(t, p):
    tl = len(t)
    pl = len(p)
    
    return len([t[i:pl+i] for i in range(tl) if t[i:pl+i] <= p and len(t[i:pl+i])==pl])