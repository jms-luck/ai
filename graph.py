def graph_coloring(graph):
    colors = [-1] * len(graph)  
    colors[0] = 0 
    for node in range(1, len(graph)):
        available_colors = [True] * len(graph)  
        for neighbor in graph[node]:
            if colors[neighbor] != -1: 
                available_colors[colors[neighbor]] = False
        for color in range(len(graph)):
            if available_colors[color]: 
                colors[node] = color  
                break
    return [color + 1 for color in colors]  
graph = [
    [1, 2],
    [0, 2],
    [0, 1],
    []     
]
colors = graph_coloring(graph)
print(" ".join(map(str, colors)))
