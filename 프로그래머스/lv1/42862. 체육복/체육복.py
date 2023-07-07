def solution(n, lost, reserve):
    reserve_new = sorted([i for i in reserve if i not in lost])
    lost_new = sorted([i for i in lost if i if i not in reserve])
    a = []
    answer = n - len(lost_new)
    for i in lost_new:
        if i-1 in reserve_new:
            reserve_new.remove(i-1)
            answer +=1            
        elif i+1 in reserve_new:
            reserve_new.remove(i+1)
            answer+=1
    return answer