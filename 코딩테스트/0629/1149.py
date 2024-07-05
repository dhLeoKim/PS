import sys
sys.stdin = open('input_1149.txt')
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

# i번째를 {1:빨, 2:파, 0:초}으로 할 때, 현재까지의 비용 최솟값

for i in range(1, N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][2], dp[i-1][0])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))