import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop, heappush

def dijkstra(i, j):
    h = []
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    d[0][0] = 0
    heappush(h, (0, i, j))
    while h:
        d_ij, i, j = heappop(h)
        if d[i][j] < d_ij:
            continue
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                diff = lst[ni][nj] - lst[i][j]
                if diff < 0:
                    diff = 0
                w = diff + d_ij + 1
                if w < d[ni][nj]:
                    d[ni][nj] = w
                    heappush(h, (w, ni, nj))

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    INF = 1e9
    d = [[INF]*N for _ in range(N)]

    dijkstra(0, 0)

    print(f'#{case}', d[N-1][N-1])