import sys
sys.stdin = open('input_10026.txt')
input = sys.stdin.readline

from collections import deque

def bfs1(i, j, color):
    queue1 = deque()
    queue1.append((i, j))
    visited1[i][j] = True
    while queue1:
        i, j = queue1.popleft()
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<= ni < N and 0<= nj < N and not visited1[ni][nj] and lst[ni][nj] == color:
                queue1.append((ni, nj))
                visited1[ni][nj] = True


def bfs2(i, j, color):
    queue2 = deque()
    queue2.append((i, j))
    visited2[i][j] = True
    while queue2:
        i, j = queue2.popleft()
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<= ni < N and 0<= nj < N and not visited2[ni][nj]:
                if lst[ni][nj] == color or (color != 'B' and lst[ni][nj] != 'B'):
                    queue2.append((ni, nj))
                    visited2[ni][nj] = True


N = int(input())
lst = [list(input().strip()) for _ in range(N)]

visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]

cnt1 = cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs1(i, j, lst[i][j])
            cnt1 += 1
        if not visited2[i][j]:
            bfs2(i, j, lst[i][j])
            cnt2 += 1

print(cnt1, cnt2)