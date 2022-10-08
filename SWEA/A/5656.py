import sys
sys.stdin = open('input_5656.txt')

from itertools import product

def f(i, j, val):
    di, dj = [1, 0, 0], [0, 1, -1]
    stack = []
    stack.append((i, j, val))
    arr[i][j] = 0
    while stack:
        i, j, val = stack.pop()
        if val == 0:
            break

    return

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(H)]

    if tc != 1:
        continue
    print(N)
    for row in lst:
        print(row)

    for case in product(range(W), repeat=N):
        arr = []
        for row in lst:
            arr.append(row[:])

        for j in case:
            for i in range(H):
                if arr[i][j]:
                    f(i, j, arr[i][j]-1)
                    break

            else:
                break

    print(f'#{tc}')