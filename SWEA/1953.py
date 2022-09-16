import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def nxts(i, j):                     # 파이프 번호별 탐색해야할 방향 반환
    now = lst[i][j]
    if now == 1:
        nxt = [0, 1, 2, 3]
    elif now == 2:
        nxt = [0, 2]
    elif now == 3:
        nxt = [1, 3]
    else:
        nxt = [now%4, (now+1)%4]

    return nxt

def bfs(i, j):
    global ret
    queue = deque()
    queue.append((i, j))
    ret = 1
    time[i][j] = 1
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
    while queue:
        i, j = queue.popleft()
        nxt = nxts(i, j)                        # 가능한 다음 방향 경우
        for k in nxt:
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] in tunnel[k] and time[ni][nj] == -1:
                time[ni][nj] = time[i][j] + 1
                if time[ni][nj] <= L:           # L시간 까지만 진행
                    ret += 1
                    queue.append((ni, nj))

    return ret

T = int(input())
for case in range(1, T+1):
    N, M, i, j, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    tunnel = [              # 상좌하우에 존재가능한 파이프 번호 경우의 수
        [1, 2, 5, 6],
        [1, 3, 6, 7],
        [1, 2, 4, 7],
        [1, 3, 4, 5]
    ]

    time = [[-1]*M for _ in range(N)]
    ret = bfs(i, j)         # bfs, L시간 동안 진행한 칸 반환

    print(f'#{case} {ret}')