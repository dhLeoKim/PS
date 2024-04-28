from collections import deque

def solution(n, edge):

    def bfs(now):
        queue = deque()
        queue.append(now)
        visited[now] = 0
        while queue:
            now = queue.popleft()
            for nxt in adj[now]:
                if visited[nxt] == -1:
                    queue.append(nxt)
                    visited[nxt] = visited[now] + 1
    
    
    adj = [[]*(n+1) for _ in range(n+1)]

    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)

    visited = [-1]*(n+1)
    bfs(1)

    print(visited)

    maxd = 0
    ret = 0
    for dis in visited:
        if dis > maxd:
            maxd = dis
            ret = 1
        elif dis == maxd:
            ret += 1

    return ret

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(vertex))