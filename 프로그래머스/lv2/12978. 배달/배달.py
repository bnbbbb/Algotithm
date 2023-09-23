import heapq
def solution(n, road, k):
    graph = [[] for _ in range(n)]
    for a, b, c in road:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
    dist = [float('inf')] * n
    dist[0] = 0
    
    pq = [(0,0)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    answer = 0
    for distance in dist:
        if distance <= k:
            answer += 1
    return answer