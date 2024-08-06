import sys
sys.stdin = open('input_11000.txt')
input = sys.stdin.readline

from heapq import*

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

room = [0]
for i in range(N):
    if lst[i][0] >= room[0]:
        heappop(room)
        heappush(room, lst[i][1])
    else:
        heappush(room, lst[i][1])

print(len(room))