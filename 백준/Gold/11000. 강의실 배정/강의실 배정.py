import sys
import heapq
input = sys.stdin.readline

N = int(input())
edus = []

for _ in range(N):
    edus.append(list(map(int,input().split())))
edus.sort(key=lambda x : (x[0],x[1]))

rooms = [edus[0][1]]
for i in range(1,N):
    if rooms[0] <= edus[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms,edus[i][1])

print(len(rooms))
