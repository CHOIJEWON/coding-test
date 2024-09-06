import sys

N = int(sys.stdin.readline().strip())
count = 1

temp = True

number = []
stk = []
answer_arr = []

for i in range(N):
    target = int(sys.stdin.readline().strip())

    while count <= target:
        stk.append(count)
        answer_arr.append('+')
        count += 1

    if stk[-1] == target:
        stk.pop()
        answer_arr.append('-')
    else:
        temp = False
        break

if not temp:
    print('NO')
else:
    for answer in answer_arr:
        print(answer)
