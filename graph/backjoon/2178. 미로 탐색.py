import sys
from collections import deque

col, row = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(col)]

visited = [[False] * row for _ in range(col)]
queue = deque()
queue.append((0, 0, 1))
visited[0][0] = True

while queue:
    cur_y, cur_x, cur_cnt = queue.popleft()

    if cur_y == col - 1 and cur_x == row - 1:
        print(cur_cnt)
        break

    # 상하좌우 방향
    ny = [-1, 1, 0, 0]
    nx = [0, 0, -1, 1]
    for i in range(4):
        next_y = cur_y + ny[i]
        next_x = cur_x + nx[i]

        if 0 <= next_x < row and 0 <= next_y < col:
            if not visited[next_y][next_x] and graph[next_y][next_x] == 1:
                visited[next_y][next_x] = True
                queue.append((next_y, next_x, cur_cnt + 1))