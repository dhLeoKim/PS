import sys
sys.stdin = open("input_1932.txt")
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][0]
        elif j == len(dp[i])-1:
            dp[i][j]+=dp[i-1][-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
            
print(max(dp[-1]))