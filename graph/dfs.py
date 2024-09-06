
def dfs(graph, start_vertex, visited):
    visited.append(start_vertex)
    for v in graph[start_vertex]:
        if v not in visited:
            visited = dfs(graph, start_vertex, visited)
    return visited

