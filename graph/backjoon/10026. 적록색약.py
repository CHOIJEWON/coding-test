import sys
from collections import deque

N = int(sys.stdin.readline().strip())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
q = deque()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x):
    visited[y][x] = True
    q.append((y, x))

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0 <= next_y < N and 0 <= next_x < N:
                if graph[cur_y][cur_x] == graph[next_y][next_x]:
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        q.append((next_y, next_x))
# 색약이 아닌 사람
visited = [[False] * N for _ in range(N)]
cnt1 = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x)
            cnt1 += 1

for y in range(N):
    for x in range(N):
        if graph[y][x] == 'G':
            graph[y][x] = 'R'

visited = [[False] * N for _ in range(N)]
cnt2 = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x)
            cnt2 += 1

print(cnt1, cnt2)