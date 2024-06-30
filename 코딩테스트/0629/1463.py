import sys
sys.stdin = open('input_1463.txt')
input = sys.stdin.readline

X = int(input())
dp = [0]*1000005

# 초기화
dp[0] = 0
dp[1] = 0

for i in range(2, X+1):

    # -1, //2, //3 연산 비교
    dp[i] = dp[i-1] + 1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X])