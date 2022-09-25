import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs():
    while queue:
        i, j, t = queue.popleft()

        if t == M: return

        n, d = lst[i][j]

        if n == 0: continue

        ni, nj = i+di[d], j+dj[d]
        if 0 < ni < N-1 and 0 < nj < N-1:
            lst_nxt[ni][nj] = (n, d)
            queue.append((ni, nj, t+1))
        else:
            lst_nxt[ni][nj] = (n//2, d+1 if d%2 else d-1)
            queue.append((ni, nj, t+1))

T = int(input())
for case in range(1, T+1):
    N, M, K = map(int, input().split())

    di, dj = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    lst = [[0]*N for _ in range(N)]
    lst_nxt = [[0]*N for _ in range(N)]
    queue = deque()
    for _ in range(K):
        i, j, n, d = map(int, input().split())
        queue.append((i, j, 0))
        lst[i][j] = (n, d)

    print(queue)
    print(lst)

    bfs()


    print(f'#{case}')

    break