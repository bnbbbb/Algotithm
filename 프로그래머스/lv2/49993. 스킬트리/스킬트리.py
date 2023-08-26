def solution(skill, skill_trees):
    answer = 0
    
    for ski in skill_trees:
        stack = ''
        for i in range(len(ski)):
            if ski[i] in skill:
                stack += ski[i]
        if stack == skill or stack == skill[:len(stack)]:
            answer += 1
    return answer