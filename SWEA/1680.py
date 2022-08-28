import sys
sys.stdin = open('input.txt')

T = int(input())
T = 1
for case in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    t = max(lst)
    custom = [0]*(t+1)

    for i in lst:
        custom[i] += 1
        