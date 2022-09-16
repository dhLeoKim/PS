import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = visited[now] + 1     # visited에 깊이 기록

T = 10
for case in range(1, 11):
    N, s = map(int, input().split())
    lst = list(map(int, input().split()))

    visited = [0]*101
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):                        # 인접 리스트로 저장
        graph[lst[i]].append(lst[i+1])

    bfs(s)                                          # bfs

    max_val = 0
    ret = 0
    for i in range(len(visited)):                   # 최대값 찾기
        if visited[i] >= max_val:
            max_val = visited[i]
            ret = i

    print(f'#{case} {ret}')