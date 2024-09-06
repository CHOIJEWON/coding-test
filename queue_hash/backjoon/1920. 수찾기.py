import sys
N = int(sys.stdin.readline().strip())
A = list((str(sys.stdin.readline().strip()).replace(" ", "")))
M = int(sys.stdin.readline().strip())
number = list(''.join(str(sys.stdin.readline().strip()).replace(" ", "")))

number_dict = {A[i]:True for i in range(N)}

for i in range(M):
    if number[i] in number_dict:
        print('1')
    else:
        print('0')

