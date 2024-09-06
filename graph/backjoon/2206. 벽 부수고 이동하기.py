from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
q.append((0, 0, 0))

while q:
    cur_y, cur_x, cur_break = q.popleft()

    if cur_y == N - 1 and cur_x == M - 1:
        print(visited[cur_y][cur_x][cur_break] + 1)
        exit()

    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]

        if 0 <= next_y < N and 0 <= next_x < M:
            if graph[next_y][next_x] == 1 and cur_break == 0:
                visited[next_y][next_x][1] = visited[cur_y][cur_x][cur_break] + 1
                q.append((next_y, next_x, 1))

            elif graph[next_y][next_x] == 0 and visited[next_y][next_x][cur_break] == 0:
                visited[next_y][next_x][cur_break] = visited[cur_y][cur_x][cur_break] + 1
                q.append((next_y, next_x, cur_break))

print(-1)

