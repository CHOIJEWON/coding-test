import sys

pipe = list(str(sys.stdin.readline().strip()))
pipe_length = len(pipe)

count = 0
result = 0
stk = []

while count < pipe_length:
    current_pipe = pipe[count]

    if count < pipe_length - 1:
        next_pipe = pipe[count + 1]
    else:
        next_pipe = ''

    if current_pipe == '(' and next_pipe == ')':
        result += len(stk)
        count += 2

    elif current_pipe == '(' and next_pipe != ')':
        stk.append(current_pipe)
        count += 1

    else:
        stk.pop()
        result += 1
        count += 1

print(result)
