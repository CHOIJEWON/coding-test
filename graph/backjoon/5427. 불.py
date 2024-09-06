import sys
from collections import deque

CASE = int(sys.stdin.readline().strip())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(CASE):
    W, H = map(int, sys.stdin.readline().split())
    graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(H)]

    visited = [[0] * W for _ in range(H)]
    q = deque()

    temp_dict = {
        '@': [],
        '*': [],
    }

    for y in range(H):
        for x in range(W):
            if graph[y][x] == '@':
                if y == 0 or y == H - 1 or x == 0 or x == W - 1:
                    print(1)
                    continue
                temp_dict['@'].append((y, x, '@'))
                visited[y][x] = 1
            elif graph[y][x] == '*':
                temp_dict['*'].append((y, x, '*'))

    q.append(temp_dict['@'].pop())

    for _ in range(len(temp_dict['*'])):
        q.append(temp_dict['*'].pop())

    while q:
        cur_y, cur_x, who = q.popleft()

        if who == '@' and graph[cur_y][cur_x] == '*':
            continue

        if who == '@':
            if cur_y == 0 or cur_y == H - 1 or cur_x == 0 or cur_x == W - 1:
                print(visited[cur_y][cur_x])
                break

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0 <= next_y < H and 0 <= next_x < W:
                if who == '@':
                    if graph[next_y][next_x] == '.' and visited[next_y][next_x] == 0:
                        is_safe = True
                        for j in range(4):
                            temp_next_y = next_y + dy[j]
                            temp_next_x = next_x + dx[j]

                            if 0 <= temp_next_y < H and 0 <= temp_next_x < W:
                                if graph[temp_next_y][temp_next_x] == '*':
                                    is_safe = False
                                    break

                        if not is_safe:
                            continue
                        elif is_safe:
                            visited[next_y][next_x] = visited[cur_y][cur_x] + 1
                            q.append((next_y, next_x, '@'))

                elif who == '*':
                    if graph[next_y][next_x] != '*' and graph[next_y][next_x] != '#':
                        graph[next_y][next_x] = '*'
                        q.append((next_y, next_x, '*'))
    else:
        print('IMPOSSIBLE')