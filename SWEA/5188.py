import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = lst[0][0]

    for i in range(N):
        for j in range(N):
            di, dj = [-1, 0], [0, -1]
            temp = []
            for k in range(2):
                pi, pj = i+di[k], j+dj[k]
                if 0 <= pi < N and 0 <= pj < N:
                    temp.append(dp[pi][pj])

            if temp:
                dp[i][j] = lst[i][j] + min(temp)

    print(f'#{case} {dp[N-1][N-1]}')