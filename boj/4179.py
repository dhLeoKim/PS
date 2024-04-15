import sys
sys.stdin = open('input_4179.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start, fire):
    queue = deque()

    si, sj = start[0], start[1]
    queue.append((False, si, sj, 1))
    lst[si][sj] = 1
    visited[si][sj] = '.'

    # if si == 0 or si == R-1 or sj == 0 or sj == C-1:
    #     return 1

    for fi, fj in fire:
        queue.append((True, fi, fj, 1))
        visited[fi][fj] = 'F'

    while queue:
        isFire, i, j, t = queue.popleft()

        if not isFire and visited[i][j] != 'F' and (i == 0 or i == R-1 or j == 0 or j == C-1):
            return t

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if isFire and visited[ni][nj] == '.':
                    visited[ni][nj] = 'F'
                    queue.append((True, ni, nj, t+1))
                elif not isFire and lst[ni][nj] == '.' and visited[ni][nj] != 'F' and visited[i][j] != 'F':
                    lst[ni][nj] = t+1
                    queue.append((False, ni, nj, t+1))

    return 'IMPOSSIBLE'


R, C = map(int, input().split())
lst = []
visited = []
fire = []
for i in range(R):
    row = list(input().strip())
    lst.append(row[:])
    visited.append(row[:])
    for j in range(C):
        if row[j] == 'J':
            start = [i, j]
        elif row[j] == 'F':
            fire.append((i, j))

di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]

ret = bfs(start, fire)

print(ret)