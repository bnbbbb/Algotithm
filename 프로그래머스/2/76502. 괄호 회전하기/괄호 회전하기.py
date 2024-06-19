def solution(s):
    answer = 0
    n = 0
    a = ''
    stack = []
    while n != len(s):
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    break
                cur = stack.pop()
                if i == ')' and cur != '(':
                    break
                
                elif i == '}' and cur != '{':
                    break
                
                elif i == '[' and cur != '[':
                    break
        else:
            if not stack:
                answer+=1
        n += 1
        a = s[0]
        s = s[1:]
        s += a
    return answer