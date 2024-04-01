from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    if max(max(queue1), max(queue2)) > (sum_que1 + sum_que2) // 2 or (sum_que1 + sum_que2) % 2 != 0:
        return -1
    max_iterations = 300000
    while sum_que1 != sum_que2:
        if sum_que1 > sum_que2:
            element = queue1.popleft()
            queue2.append(element)
            sum_que2 += element
            sum_que1 -= element
        else:
            element = queue2.popleft()
            queue1.append(element)
            sum_que1 += element
            sum_que2 -= element
        if answer >= max_iterations:
            return -1
        answer +=1
    return answer