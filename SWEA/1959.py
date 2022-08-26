from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))

    if N < M:
        A += [0]*(M-N)
    elif N > M:
        B += [0]*(N-M)

    ret = []
    for _ in range(abs(N-M)+1):        
        ret.append(sum(x*y for x, y in zip(A, B)))
        # A.rotate()
        if N < M:
            A.rotate()
        else:
            B.rotate()

    print(f'#{case+1} {max(ret)}')