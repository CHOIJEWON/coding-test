import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

number_of_painting = 0
number_of_width = 0

q = deque()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    cnt = 1
    graph[y][x] = 0
    q.append((y, x))
    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0 <= next_y < n and 0 <= next_x < m:
                if graph[next_y][next_x]:
                    cnt += 1
                    graph[next_y][next_x] = 0
                    q.append((next_y, next_x))
    return cnt

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            count = bfs(y, x)
            number_of_painting += 1
            if count > number_of_width:
                number_of_width = count

print(number_of_painting)
print(number_of_width)