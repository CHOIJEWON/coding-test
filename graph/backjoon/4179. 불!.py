import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

q = deque()

temp_dict = {
    'J': [],
    'F': [],
}
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
distance = [[0] * C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if graph[y][x] == 'J':
            # 각 테두리에 존재하면 다음 턴이 탈출임
            if y == 0 or x == 0 or y == R -1 or x == C -1:
                print(1)
                exit()
            temp_dict['J'].append((y, x, 'J'))
        if graph[y][x] == 'F':
            temp_dict['F'].append((y, x, 'F'))

q.append(temp_dict['J'].pop())

for tuple in temp_dict['F']:
    q.append(tuple)

while q:
    cur_y, cur_x, what = q.popleft()

    if what == 'J' and graph[cur_y][cur_x] == 'F':
        continue

    if what == 'J' and (cur_y == 0 or cur_x == 0 or cur_y == R - 1 or cur_x == C - 1):
        print(distance[cur_y][cur_x] + 1)
        exit()

    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]

        if 0 <= next_y < R and 0 <= next_x < C:
            if what == 'J':
                if graph[next_y][next_x] == '.':
                    graph[next_y][next_x] = 'J'
                    distance[next_y][next_x] = distance[cur_y][cur_x] + 1
                    q.append((next_y, next_x, 'J'))
            elif what == 'F':
                if graph[next_y][next_x] != '#' and graph[next_y][next_x] != 'F':
                    graph[next_y][next_x] = 'F'
                    q.append((next_y, next_x, 'F'))

print('IMPOSSIBLE')