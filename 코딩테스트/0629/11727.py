import sys
sys.stdin = open("input_11727.txt")
input = sys.stdin.readline

N = int(input())
dp = [0]*1005
dp[1] = 1
dp[2] = 3

if N >= 3:
    for i in range(3, N+1):
        dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[N]%10007)