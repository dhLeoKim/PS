import sys
sys.stdin = open('input_1767.txt')

def dfs(idx):
    if idx == end:
        return
    i, j = start[idx]
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    for k in range(4):
        connect(k)
        dfs(idx+1)
        
        # while True:
        #     if i == 0 or i == N-1 or j == 0 or j == N-1:
        #         dfs(idx+1)
        #         break
        #     ni, nj = i+di[k], j+dj[k]
        #     if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 0:
        #         lst[ni][nj] = 1
        #         i, j = ni, nj


    # for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
    #     ni, nj = i+di, j+dj
    #     if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 0:


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # cell = [[0]*N for _ in range(N)]

    start = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if lst[i][j]:
                start.append((i, j))

    end = len(start)
    dfs(0)

    print(f'#{tc}')

    break