from collections import deque

def convert_A_to_B(A, B):
    queue = deque([(A, 0)])  
    visited = set() 

    while queue:
        current, count = queue.popleft()
        if current == B:
            return count + 1

        doubled = current * 2
        if doubled <= B and doubled not in visited:
            queue.append((doubled, count + 1))
            visited.add(doubled)
            

        appended = current * 10 + 1
        if appended <= B and appended not in visited:
            queue.append((appended, count + 1))
            visited.add(appended)

    return -1

A, B = map(int, input().split())

result = convert_A_to_B(A, B)
print(result)