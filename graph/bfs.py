from collections import deque


def bfs(graph, start_vertex):
    visited = [start_vertex]
    queue = deque(start_vertex)
    while queue:
        current_vertex = queue.popleft()
        for v in graph[current_vertex]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

