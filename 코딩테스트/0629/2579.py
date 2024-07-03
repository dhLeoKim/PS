import sys
sys.stdin = open('input_2579.txt')
input = sys.stdin.readline

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

dp = [0]*(N+1)

dp[0] = lst[0]
dp[1] = lst[0] + lst[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

print(dp[N])