from collections import deque

grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]


def shortest_distance(grid):
    n = len(grid[0])
    visited = [[False] * n for _ in range(n)]

    shortest_len = -1

    if grid[0][0] or grid[n - 1][n - 1] == 1:
        return -1

    move = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_count = queue.popleft()

        if cur_r == n-1 and cur_c == n-1:
            shortest_len = cur_count
            break

        for dr, dc in move:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if 0 <= next_r < n and 0 <= next_c < n:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_count + 1))
                    visited[next_r][next_c] = True

    return shortest_len

print(shortest_distance(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
