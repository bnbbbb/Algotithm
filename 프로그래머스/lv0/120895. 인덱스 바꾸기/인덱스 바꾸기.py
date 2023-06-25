def solution(st, n1, n2):
    return st[:n1] + st[n1:n2+1][-1] + st[n1+1:n2] + st[n1:n2+1][0] + st[n2+1:]