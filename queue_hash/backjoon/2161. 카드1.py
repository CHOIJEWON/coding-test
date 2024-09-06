import sys
from collections import deque

N = int(sys.stdin.readline().strip())
trash = []
card = deque(index for index in range(1, N+1))

while len(card) > 1:
    throw_card = card.popleft()
    trash.append(throw_card)
    second_card = card.popleft()
    card.append(second_card)

trash.append(card.popleft())

print(*trash)


