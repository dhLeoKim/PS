from collections import deque

def solution(maps):
    
    def bfs():
        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True
        
        while queue:
            i, j, l = queue.popleft()
            
            if i == N-1 and j == M-1:
                return l
            
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] and not visited[ni][nj]:
                    queue.append((ni, nj, l+1))
                    visited[ni][nj] = True
        
        return -1
        
    
    N = len(maps)
    M = len(maps[0])
    visited = [[False]*M for _ in range(N)]
    
    di, dj = [0, 1, 0 ,-1], [1, 0, -1, 0]
    
    ret = bfs()

    return ret

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))