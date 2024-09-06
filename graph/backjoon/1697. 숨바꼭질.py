import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

matrix = [False] * 100000

matrix[N] = True

queue = deque()
queue.append((N, 0))

while queue:
    cur_position, cur_cnt = queue.popleft()

    moving = [-1, +1, cur_position]
    if cur_position == K:
        print(cur_cnt)
        break

    for i in range(3):
        next_position = cur_position + moving[i]

        if N < next_position <= 100000 and cur_position + cur_position < 100000:
            if not matrix[next_position]:
                matrix[next_position] = True
                queue.append((next_position, cur_cnt + 1))

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

matrix = [False] * 100001  # 0부터 100000까지 인덱스 사용

matrix[N] = True

queue = deque()
queue.append((N, 0))

while queue:
    cur_position, cur_cnt = queue.popleft()

    moving = [-1, +1, cur_position]
    if cur_position == K:
        print(cur_cnt)
        break

    for i in range(3):
        if i == 2:
            next_position = cur_position * 2
        else:
            next_position = cur_position + moving[i]

        if 0 <= next_position <= 100000 and not matrix[next_position]:
            matrix[next_position] = True
            queue.append((next_position, cur_cnt + 1))