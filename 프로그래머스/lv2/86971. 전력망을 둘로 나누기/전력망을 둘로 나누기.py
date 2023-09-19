def dfs(node, graph, visited):
    visited[node] = True
    subnetwork_size = 1 
    
    for i in graph[node]:
        if not visited[i]:
            subnetwork_size += dfs(i, graph, visited)
    
    return subnetwork_size

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    min_difference = n
    
    for wire in wires:
        v1, v2 = wire
        visited = [False] * (n + 1)
        visited[v1] = True
        subnetwork_size1 = dfs(v2, graph, visited)
        subnetwork_size2 = n - subnetwork_size1
        
        difference = abs(subnetwork_size1 - subnetwork_size2)
        min_difference = min(min_difference, difference)
    return min_difference