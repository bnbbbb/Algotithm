def solution(s):
    result = ''
    s_len = len(s)
    idx  = 1
    queue = []
    if len(s) == 1:
        return 1
    while idx != s_len:
        st = ''
        answer = 0
        stack = []
        result = ''
        for i in range(0, s_len, idx):
            result = s[i+idx:i+idx+idx]
            stack.append(s[i:i+idx])
            if stack[0] !=  result:
                if answer != 0:
                    st += str(answer+1) + stack[0]
                else:
                    st += stack[0]
                
                stack = []
                answer = 0
            else:
                answer += 1
        queue.append(st)
        idx += 1
    queue.sort(key=lambda x: len(x))
    return len(queue[0])