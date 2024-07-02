import sys
sys.stdin = open('input_9095.txt')
input = sys.stdin.readline

T = int(input())

tc = []
for _ in range(T):
    N = int(input())
    tc.append(N)

########################

# dp = [0]*13

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4, 12):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# for idx in tc:
#     print(dp[idx])

########################

# dp[i] = i를 만들 때 [1을 더하는 경우, 2를 더하는 경우, 3을 더하는 경우]
dp = [[0, 0, 0] for _ in range(13)]

dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 1, 1]

for i in range(4, 13):
    dp[i][0] = sum(dp[i-1])     # i-1에 1을 더해 i를 만드는 방법
    dp[i][1] = sum(dp[i-2])     # i-2에 2를 더해 i를 만드는 방법
    dp[i][2] = sum(dp[i-3])     # i-3에 3을 더해 i를 만드는 방법

for idx in tc:
    print(sum(dp[idx]))