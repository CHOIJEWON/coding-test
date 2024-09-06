import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
count = 0

def dfs(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count-1)