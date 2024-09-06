from collections import deque

def number_of_island(grid):
    island_number = 0
    x_len = len(grid[0]) # 가로축 = 5
    y_len = len(grid) # 세로축 = 4
    visited = [[False] * x_len for _ in range(y_len)]

    def bfs(y, x):
        visited[y][x] = True
        queue = deque()
        queue.append((x, y))
        # dy = []
        # dx = []
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if 0 <= next_x < y_len and 0 <= next_y < x_len and grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

    for y in range(y_len): # 행
        for x in range(x_len): # 열
            if grid[y][x] == '1' and not visited[y][x]: # [y][x]
                bfs(y, x)
                island_number += 1

    return island_number

