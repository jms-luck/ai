from heapq import heappop, heappush

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('E', 3)],
    'D': [('B', 2), ('DG', 1)],
    'E': [('B', 5), ('C', 3), ('DG', 6)],
    'DG': [('D', 1), ('E', 6)]
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'DG': 0
}

def a_star(start, goal='DG'):
    pq, visited = [(heuristic[start], 0, start, [])], set()
    
    while pq:
        _, cost, node, path = heappop(pq)
        
        if node == goal:
            return path + [node]
        
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heappush(pq, (cost + weight + heuristic[neighbor], cost + weight, neighbor, path + [node]))
    
    return None

start = 'A'
result = a_star(start)
print(f"Path found: {result}")
