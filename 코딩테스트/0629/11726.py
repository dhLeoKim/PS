import sys
sys.stdin = open('input_11726.txt')
input = sys.stdin.readline

N = int(input())
dp = [0]*1002

dp[1] = 1
dp[2] = 2

# i번째까지 채우는 방법의 수 : i-1 + 1칸, i-2 + 2칸
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]   

print(dp[N]%10007)