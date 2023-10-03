def solution(p):
    if not p:
        return ""
    
    u, v = split_p(p)
    
    if correct(u):
        return u + solution(v)
    
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        u = reverse(u)
        answer += u
        return answer
def split_p(p):
    left_count = 0
    right_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            return p[:i + 1], p[i + 1:]

def correct(u):
    stack = []
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def reverse(u):
    result =""
    for char in u:
        if char == '(':
            result += ')'
        else:
            result += '('
    return result