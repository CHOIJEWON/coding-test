import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

def dfs(start_node):
    visited[start_node] = True
    for next_node in graph[start_node]:
        if not visited[next_node]:
            dfs(next_node)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt +=1

print(cnt)


