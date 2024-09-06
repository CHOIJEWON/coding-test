import sys
from collections import deque

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
number_of_house = 0
house_width = []

def bfs(y, x):
    visited[y][x] = True
    ny = [-1, 1, 0, 0]
    nx = [0, 0, -1, 1]

    queue = deque()
    queue.append((y, x))
    width = 1
    while queue:
        cur_y, cur_x = queue.popleft()

        for i in range(4):
            next_y = cur_y + ny[i]
            next_x = cur_x + nx[i]

            if 0 <= next_y < N and 0 <= next_x < N:
                if not visited[next_y][next_x] and graph[next_y][next_x] == 1:
                    width += 1
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
    house_width.append(width)


for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and not visited[y][x]:
            bfs(y, x)
            number_of_house += 1
        elif graph[y][x] == 0:
            visited[y][x] = True

house_width.sort()
print(number_of_house)
print("\n".join(map(str, house_width)))

