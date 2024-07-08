import sys
sys.stdin = open('input_12852.txt')
input = sys.stdin.readline

N = int(input())

p = [0]*1000005
dp = [0]*1000005
dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    p[i] = i-1 

    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        p[i] = i//3

    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        p[i] = i//2


print(dp[N])
print(N, end=' ')
for i in range(dp[N]):
    print(p[N], end=' ')
    N = p[N]