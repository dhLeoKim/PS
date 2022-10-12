import sys
sys.stdin = open('input_1949.txt')

def dfs(i, j, l, t):
    global ret
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and not visitied[ni][nj]:
            if lst[ni][nj] < lst[i][j]:                 # 다음 수가 작으면 진행
                visitied[ni][nj] = True
                dfs(ni, nj, l+1, t)
                visitied[ni][nj] = False
            elif t:
                diff = lst[ni][nj] - (lst[i][j]-1)
                if diff <= K:                           # 다음 수가 크지만, 깎을 수 있을 때
                    lst[ni][nj] -= diff
                    visitied[ni][nj] = True
                    dfs(ni, nj, l+1, False)
                    lst[ni][nj] += diff
                    visitied[ni][nj] = False

    if l > ret:                                         # 최대값 업데이트
        ret = l

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    start = []                                          # 시작점 찾아서 저장
    for i in range(N):
        for j in range(N):
            if lst[i][j] > max_val:
                start = [(i, j)]
                max_val = lst[i][j]
            elif lst[i][j] == max_val:
                start.append((i, j))

    ret = 0
    for i, j in start:
        visitied = [[False]*N for _ in range(N)]
        visitied[i][j] = True
        dfs(i, j, 1, True)

    print(f'#{tc}', ret)