def convert(n, base):
    if n == 0:
        return "0"
    
    T = "0123456789ABCDEF"
    result = ''

    while n > 0:
        remainder = n % base
        result = T[remainder] + result
        n //= base
    
    return result

def solution(n, t, m, p):
    answer = ''
    
    for i in range(t * m): 
        converted = convert(i, n)
        answer += converted
        
        if len(answer) >= t * m:  
            break
    
    result = ""
    for i in range(p - 1, t * m, m):  
        result += answer[i]
    
    return result[:t] 