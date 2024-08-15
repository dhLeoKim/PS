import sys
sys.stdin = open('input_11286.txt')
input = sys.stdin.readline

import heapq

N = int(input())
h = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])