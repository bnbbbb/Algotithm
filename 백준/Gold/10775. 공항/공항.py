import sys

g = int(sys.stdin.readline().rstrip())

p = int(sys.stdin.readline().rstrip())

count = 0

planes = [int(sys.stdin.readline().rstrip()) for _ in range(p)]

gate = [i for i in range(g+1)]


def find(plane):
    if gate[plane] == plane:
        return plane
    gate[plane] = find(gate[plane])
    return gate[plane]

for plane in planes:
    temp = find(plane)
    if temp == 0:
        break
    gate[temp] = gate[temp-1]  #게이트가 채워졌으므로 옆의 게이트로 부모 게이트를 바꿔줌
    count += 1

print(count)