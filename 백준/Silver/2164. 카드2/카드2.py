from collections import deque
s = deque(range(1, int(input())+1))
while len(s) != 1:
    s.popleft()
    s.append(s.popleft())
print(*s)