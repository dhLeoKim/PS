#####################
# 1.

import sys
sys.stdin = open('sample_input.txt')

from itertools import permutations

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ret = []
    for p in permutations(range(2, N+1), N-1):
        route = [1] + list(p) + [1]
        bat = 0
        for i in range(len(route)-1):
            bat += lst[route[i]-1][route[i+1]-1]

        ret.append(bat)

    print(f'#{case} {min(ret)}')

#####################
# 2.

import sys
sys.stdin = open('sample_input.txt')

def backtracking():
    if len(arr) == N:
        arr.append(1)
        temp = 0
        for k in range(len(arr)-1):
            temp += (lst[arr[k]-1][arr[k+1]-1])
        ret.append(temp)
        arr.pop()
        return

    for i in range(2, N+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    arr = [1]
    ret = []
    backtracking()

    print(f'#{case} {min(ret)}')