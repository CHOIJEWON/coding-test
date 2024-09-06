import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

for t in range(N):
    I = int(input().strip())
    y, x = map(int, input().strip().split())
    goal_y, goal_x = map(int, input().strip().split())

    if y == goal_y and x == goal_x:
        print(0)
        continue

    visited = [[False] * I for _ in range(I)]

    visited[y][x] = True
    queue = deque()
    queue.append((y, x, 1))

    ny = [-2, -2, +2, +2, -1, -1, +1, +1]
    nx = [-1, +1, -1, +1, -2, +2, -2, +2]

    found = False

    while queue:
        cur_y, cur_x, cur_point = queue.popleft()

        for i in range(8):
            next_y = cur_y + ny[i]
            next_x = cur_x + nx[i]

            if next_y == goal_y and next_x == goal_x:
                print(cur_point)
                found = True
                break

            if 0 <= next_x < I and 0 <= next_y < I:
                if not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x, cur_point + 1))
        if found:
            break