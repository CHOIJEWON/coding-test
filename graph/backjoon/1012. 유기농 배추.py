import sys
from collections import deque

T = int(sys.stdin.readline().strip())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[True] * M for _ in range(N)]
    q = deque()
    cnt = 0

    def bfs(y, x):
        graph[y][x] = True
        q.append((y, x))

        while q:
            cur_y, cur_x = q.popleft()

            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                if 0 <= next_y < N and 0 <= next_x < M:
                    if not graph[next_y][next_x]:
                        graph[next_y][next_x] = True
                        q.append((next_y, next_x))
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = False

    for y in range(N):
        for x in range(M):
            if not graph[y][x]:
                bfs(y, x)
                cnt += 1

    print(cnt)