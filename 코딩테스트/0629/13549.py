import sys
sys.stdin = open('input_13549.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    global ret

    queue = deque()
    queue.append((N, 0))
    visited[N] = True
    
    while queue:
        now, t = queue.popleft()

        if now == K:
            return t

        # 수빈이가 움직이는 순서가 중요!
        for nxt in [2*now, now-1, now+1]:
            if 0 <= nxt < 100005 and not visited[nxt]:
                if nxt == 2*now:
                    queue.append((nxt, t))
                    visited[nxt] = True
                else:
                    queue.append((nxt, t+1))
                    visited[nxt] = True


N, K = map(int, input().split())
visited = [False]*100005

ret = bfs()

print(ret)