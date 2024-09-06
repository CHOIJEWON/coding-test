import sys
from collections import deque

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

painting_number = 2
surround_sea_q = deque()

def spread_bfs(y, x, spread_num):
    q = deque()
    q.append((y, x))
    graph[y][x] = spread_num
    visited[y][x] = True

    while q:
        cur_y, cur_x = q.popleft()

        for k in range(4):
            next_y = cur_y + dy[k]
            next_x = cur_x + dx[k]

            if 0 <= next_y < N and 0 <= next_x < N:
                if graph[next_y][next_x] == 0 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    surround_sea_q.append((next_y, next_x, spread_num, 1))
                if graph[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    q.append((next_y, next_x))

shortest_distance = []


def shortest_distance_bfs():
    vis = [[False] * N for _ in range(N)]

    while surround_sea_q:
        cur_y, cur_x, cur_spread, cur_cnt = surround_sea_q.popleft()

        for t in range(4):
            next_y = cur_y + dy[t]
            next_x = cur_x + dx[t]

            if 0 <= next_y < N and 0 <= next_x < N:
                if graph[next_y][next_x] >= 1 and graph[next_y][next_x] != cur_spread and not vis[next_y][next_x]:
                    vis[next_y][next_x] = True
                    shortest_distance.append(cur_cnt)
                if graph[next_y][next_x] == 0 and not vis[next_y][next_x]:
                    vis[next_y][next_x] = True
                    surround_sea_q.append((next_y, next_x, cur_spread, cur_cnt + 1))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            spread_bfs(i, j, painting_number)
            shortest_distance_bfs()
            painting_number += 1

if shortest_distance:
    print(min(shortest_distance))
    exit()
else:
    print(-1)
