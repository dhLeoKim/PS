import sys
sys.stdin = open('input_1600.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))

    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    hi, hj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        i, j, k = queue.popleft()
        for l in range(4):
            ni, nj = i+di[l], j+dj[l]
            if 0 <= ni < H and 0 <= nj < W and lst[ni][nj] == 0 and visited[ni][nj][k] == -1:
                visited[ni][nj][k] = visited[i][j][k] + 1
                queue.append((ni, nj, k))
        if k < K:
            for l in range(8):
                ni, nj = i+hi[l], j+hj[l]
                if 0 <= ni < H and 0 <= nj < W and lst[ni][nj] == 0 and visited[ni][nj][k+1] == -1:
                    visited[ni][nj][k+1] = visited[i][j][k] + 1
                    queue.append((ni, nj, k+1))


K = int(input())
W, H = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(H)]

visited = [[[-1]*(K+1) for _ in range(W) ] for _ in range(H)]
visited[0][0] = [0]*(K+1)

bfs()

ret = 1e11
for res in visited[H-1][W-1]:
    if res == -1:
        continue
    else:
        ret = min(ret, res)

print(ret if ret != 1e11 else -1)