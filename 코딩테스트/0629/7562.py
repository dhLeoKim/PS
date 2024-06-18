import sys
sys.stdin = open('input_7562.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((si, sj, 0))
    visited[si][sj] = True

    while queue:
        i, j, cnt = queue.popleft()

        if i == ei and j == ej:
            return cnt

        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                queue.append((ni, nj, cnt+1))
                visited[ni][nj] = True
    
    return 0


T = int(input())
for tc in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    visited = [[False]*N for _ in range(N)]
    di, dj = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

    ret = bfs()

    print(ret)