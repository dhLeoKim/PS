import sys
sys.stdin = open('input_11659.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix_sum = [0]*(N+5)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

for _ in range(M):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i-1])