import sys
sys.stdin = open('input_2606.txt')
input = sys.stdin.readline

from collections import deque

def bfs(now):
    queue = deque()
    queue.append(now)
    visited.append(now)

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if nxt not in visited:
                queue.append(nxt)
                visited.append(nxt)


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
bfs(1)
print(len(visited)-1)