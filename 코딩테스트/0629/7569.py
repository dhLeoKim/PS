import sys
sys.stdin = open('input_7569.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    queue = deque()
    for h, i, j in start:
        queue.append((h, i, j, 1))
    
    while queue:
        h, i, j, cnt = queue.popleft()
        for k in range(6):
            nh, ni, nj = h+dh[k], i+di[k], j+dj[k]
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and lst[nh][ni][nj] == 0:
                lst[nh][ni][nj] = cnt+1
                queue.append((nh, ni, nj, cnt+1))


M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
start = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 1:
                start.append((h, i, j))

dh, di, dj = [1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, -1]

bfs(start)

ret = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 0:
                ret = -1
                print(ret)
                exit()
            else:
                ret = max(ret, lst[h][i][j])

# 처음부터 모든 토마토가 익어있는 상태이면 0을 출력시키기 위해서
# 1 부터 시작해서 결과에서 -1 해주기
print(ret-1)