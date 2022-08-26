import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(idx, cnt, res):
    global min_val, trial
    if cnt == N//2:
        trial += 1
        print(trial, res)
        if abs(res) < min_val:
            min_val = abs(res)
            # print(res)
            return

    if idx < N-1:
        dfs(idx+1, cnt+1, res - s[idx])
        dfs(idx+1, cnt, res)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
min_val = 20000000000

# total = sum([sum(lst[i]) for i in range(N)])

s = [0]*N
total = 0
for i in range(N):
    for j in range(N):
        total += lst[i][j]
        s[i] += lst[i][j]
        s[j] += lst[i][j]

trial = 0
print(s, total)
dfs(0, 0, total)
print('trial', trial)
# print(min_val)