def solution(s):
    answer = 0
    while s:
        x = s[0]
        count_x = 0
        count_not_x = 0
        idx = 0
        while idx < len(s):
            if s[idx] == x:
                count_x += 1
            else:
                count_not_x +=1
            if count_x == count_not_x:
                break
            idx += 1
        answer += 1
        s = s[idx+1:]
    print(answer)
    return answer