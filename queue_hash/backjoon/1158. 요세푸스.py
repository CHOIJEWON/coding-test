import sys

N, K = map(int, sys.stdin.readline().split())
circle = [i for i in range(1, N+1)]
stk = []

if K == 1:
    print(f'<{", ".join(str(e) for e in circle)}>')
    sys.exit()

visit_number_index = 0

while circle:
    visit_number_index += (K - 1)

    while visit_number_index > len(circle):
        visit_number_index -= len(circle)

    if visit_number_index == len(circle):
        visit_number_index -= len(circle)


    stk.append(circle.pop(visit_number_index))

print(f'<{", ".join(str(e) for e in stk)}>')