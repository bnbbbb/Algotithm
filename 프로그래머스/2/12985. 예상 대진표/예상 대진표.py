import math
def solution(n,a,b):
    result = 1
    
    while 1:
        if (a < b and b-a ==1 and a % 2 ==1) or (a > b and a-b==1 and b%2 == 1):
            return result
        else:
            n = n//2
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            result += 1