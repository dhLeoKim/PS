import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    lst = [[0] + list(map(int, input().split())) for _ in range(N)]
    lst = [[0]*(N+1)] + lst

    ret = 0
    for i in range(1, N+1):
        temp_row = [0]*(N+1)
        temp_col = [0]*(N+1)
        for j in range(1, N+1):
            if lst[i][j] == 1:
                temp_row[j] = temp_row[j-1] + lst[i][j]

            if lst[j][i] == 1:
                temp_col[j] = temp_col[j-1] + lst[j][i]

        ret += temp_row.count(K) - temp_row.count(K+1) + temp_col.count(K) - temp_col.count(K+1)

    print(f'#{case+1} {ret}')