import sys
sys.stdin = open('input.txt')

T = 10
for case in range(T):
    N = int(input())
    lst = [list(input()) for _ in range(8)]

    ret = 0
    for i in range(8):
        for j in range(8-N+1):
            row = col = 0
            for k in range(N//2):
                if lst[i][j+k] != lst[i][j+N-1-k]: break
            else: ret += 1

    for j in range(8):
        for i in range(8-N+1):
            for k in range(N // 2):
                if lst[i+k][j] != lst[i+N-1-k][j]: break
            else: ret += 1

    print(f'#{case+1} {ret}')