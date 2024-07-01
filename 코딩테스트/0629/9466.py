import sys
sys.stdin = open('input_9466.txt')
input = sys.stdin.readline

def dfs(now):
    visited[now] = True
    stack = [now]
    team = [now]

    cnt = 0
    while stack:
        now = stack.pop()
        nxt = lst[now]
        if not visited[nxt]:
            visited[nxt] = True
            stack.append(nxt)
            team.append(nxt)
        elif nxt == now:
            cnt = 1
        else:
            for idx in range(len(team)):
                if team[idx] == nxt:
                    cnt = len(team) - idx
        
    return cnt


T = int(input())

for tc in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    visited = [False]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += dfs(i)

    ret = N-cnt
    
    print(ret)

################################################

# import sys
# sys.stdin = open('input_9466.txt')
# input = sys.stdin.readline

# from collections import deque

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     lst = [0] + list(map(int, input().split()))

#     # 팀원으로 선택 받은 횟수 저장
#     rank = [0]*(N+1)
#     for x in range(1, N+1):
#         rank[lst[x]] += 1

#     # 한번도 선택받지 못한 사람 -> 팀에 속하지 못한 사람
#     queue = deque()
#     for x in range(1, N+1):
#         if rank[x] == 0:
#             queue.append(x)

#     ret = 0
#     while queue:
#         x = queue.popleft()
#         # 한번도 선택받지 못한 사람 -> 팀에 속하지 못한 사람
#         ret += 1
        
#         # 팀에 속하지 못한 사람이 지목한 사람의 rank--, 무효한 지목 제거
#         v = lst[x]
#         rank[v] -= 1
#         # rank가 0이라면, 결국엔 팀에 속하지 못한 사람
#         if rank[v] == 0:
#             queue.append(v)
    
#     print(ret)