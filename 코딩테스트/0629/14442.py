import sys
sys.stdin = open('input_14442.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    for k in range(K+1):
        visited[k][0][0] = 1

    while queue:
        i, j, cnt = queue.popleft()

        if i == N-1 and j == M-1:
            return visited[cnt][i][j]
        
        # 인덱스 실수 주의!!!
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if lst[ni][nj] == 0 and visited[cnt][ni][nj] == -1:
                    visited[cnt][ni][nj] = visited[cnt][i][j] + 1
                    queue.append((ni, nj, cnt))
                elif cnt < K and visited[cnt+1][ni][nj] == -1:
                    visited[cnt+1][ni][nj] = visited[cnt][i][j] + 1
                    queue.append((ni, nj, cnt+1))
                
    return -1


N, M, K = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[[-1]*M for _ in range(N)] for _ in range(K+1)]

ret = bfs()

print(ret)

# visited[K][N][M] 으로 생성해서 탐색하는 속도가
# visited[N][M][K] 로 생성해서 탐색하는 속도보다 빠르다
# 공간지역성 때문에 이런 차이가 발생
# 쉽게 표현하면
# 101호 -> 102호 -> 103호 -> 201호 순서의 방문이
# 101호 -> 201호 -> 301호 -> 102호 순서의 방문보다 빠르다는 느낌