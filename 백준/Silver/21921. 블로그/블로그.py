import sys

def count_visited(n, x, visited):
    count_max_visit = 1
    current_sum = sum(visited[:x])
    max_visit = current_sum

    for i in range(x, n):
        current_sum = current_sum - visited[i - x] + visited[i]

        if current_sum > max_visit:
            max_visit = current_sum
            count_max_visit = 1
        elif current_sum == max_visit:
            count_max_visit += 1
            
    return max_visit, count_max_visit

n, x = map(int, sys.stdin.readline().split())
visited = list(map(int, sys.stdin.readline().split()))

max_visit, count_max_visit = count_visited(n, x, visited)

if max_visit != 0:
    print(max_visit)
    print(count_max_visit)
else:
    print('SAD')