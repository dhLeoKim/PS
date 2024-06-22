import sys
sys.stdin = open('input_2146.txt')
input = sys.stdin.readline

from collections import deque

def bfsChkBridge(cnt):
    global ret

    queue = deque()
    for num in range(1, cnt+1):
        for si, sj in boundary[num]:
            visited[si][sj] = [0, num]
            queue.append((si, sj))

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 0:
                if visited[ni][nj][0] == 0:
                    visited[ni][nj] = [visited[i][j][0] + 1, visited[i][j][1]]
                    queue.append((ni, nj))
                elif visited[ni][nj][1] != visited[i][j][1]:
                    ret = min(ret, visited[i][j][0] + visited[ni][nj][0])


def bfsChkLand(si, sj, cnt):
    queue = deque()
    queue.append((si, sj))
    land[si][sj] = cnt
    temp_set = set()

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == 1 and land[ni][nj] == 0:
                    land[ni][nj] = cnt
                    queue.append((ni, nj))
                elif lst[ni][nj] == 0:
                    temp_set.add((i, j))

    boundary.append(list(temp_set))


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
land = [[0]*N for _ in range(N)]
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

boundary = [[]]
cnt = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1 and land[i][j] == 0:
            cnt += 1
            bfsChkLand(i, j, cnt)

ret = 1e11
visited = [[[0]*2 for _ in range(N)] for _ in range(N)]
bfsChkBridge(cnt)

print(ret)