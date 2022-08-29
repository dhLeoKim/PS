import sys
sys.stdin = open('input1.txt')

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ret = 0
    for i in range(N):
        temp_row = [0]*(M+1)
        for j in range(M):
            if lst[i][j]:
                temp_row[j+1] = temp_row[j] + lst[i][j]
        ret = max(ret, max(temp_row))

    for i in range(M):
        temp_col = [0]*(N+1)
        for j in range(N):
            if lst[j][i]:
                temp_col[j+1] = temp_col[j] + lst[j][i]
        ret = max(ret, max(temp_col))

    print(f'#{case+1} {ret}')