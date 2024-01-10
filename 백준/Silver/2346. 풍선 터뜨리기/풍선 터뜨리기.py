from collections import deque
import sys

n = int(input())
st = deque(enumerate(map(int, input().split())))
answer = []
for _ in range(n):
    idx, balloon = st.popleft()
    answer.append(idx + 1)

    if balloon < 0:
        pass
    else:
        balloon = balloon - 1
    st.rotate(-(balloon))

print(' '.join(map(str, answer)))