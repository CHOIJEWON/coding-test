import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(map(int, sys.stdin.readline().split())) #1
stack = []
out_num = 1

while queue:
    if queue[0] == out_num:
        out_num += 1
        queue.popleft()

    else:
        stack.append(queue.popleft())

    while stack and stack[-1] == out_num:
        stack.pop()
        out_num += 1

print('Nice' if not stack else 'Sad')