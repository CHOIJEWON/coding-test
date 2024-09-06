import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
graph = []
queue = deque()

for _ in range(col):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for y in range(col):
    for x in range(row):
        if graph[y][x] == 1:
            queue.append((y, x))

while queue:
    cur_y, cur_x = queue.popleft()
    ny = [1, -1, 0, 0]
    nx = [0, 0, 1, -1]

    for i in range(4):
        next_y = cur_y + ny[i]
        next_x = cur_x + nx[i]

        if 0 <= next_x < row and 0 <= next_y < col:
            if graph[next_y][next_x] == 0:
                graph[next_y][next_x] = graph[cur_y][cur_x] + 1
                queue.append((next_y, next_x))
answer = 0

for box in graph:
    for tomato in box:
        if tomato == 0:
            print(-1)
            exit()
    answer = max(answer, max(box))

print(answer - 1)
