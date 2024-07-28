import sys
sys.stdin = open('input_1025.txt')
input = sys.stdin.readline

from math import sqrt

N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]

ret = -1
for i in range(N):
    for j in range(M):
        for di in range(-N, N):
            for dj in range(-M, M):

                if di == 0 and dj == 0:
                    continue

                ni = i
                nj = j
                temp = 0
                while 0 <= ni < N and 0 <= nj < M:
                    temp = 10*temp + lst[ni][nj]

                    if temp > ret and int(sqrt(temp))**2 == temp:
                        ret = max(ret, temp)

                    ni += di
                    nj += dj

print(ret)