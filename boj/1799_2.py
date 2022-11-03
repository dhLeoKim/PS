import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bishop(d1, ret):
    global max_v
    if d1 == M:
        if ret > max_v:
            max_v = ret
        return
    
    if ret+M-d1 <= max_v:
        return

    for d2 in range(len(arr[d1])):
        i, j = arr[d1][d2]
        if not visited[j-i+N-1]:
            visited[j-i+N-1] = True
            bishop(d1+1, ret+1)
            visited[j-i+N-1] = False
    
    bishop(d1+1, ret)


N = int(input())
M = 2*N - 1
lst = [list(map(int, input().split())) for _ in range(N)]
arr = [[] for _ in range(M)]

for j in range(N):
    for i in range(N):
        if lst[i][j]:
            arr[i+j].append((i, j))

visited = [False]*(M)
max_v = 0

bishop(0, 0)
print(max_v)
