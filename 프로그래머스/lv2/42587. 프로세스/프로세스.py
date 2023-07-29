from collections import deque

def solution(priorities, location):
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    cnt = 0

    while queue:
        current_priority, current_idx = queue.popleft()
        if any(current_priority < priority for priority, _ in queue):
            queue.append((current_priority, current_idx))
        else:
            cnt += 1
            if current_idx == location:
                return cnt