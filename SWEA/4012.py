####################
# 1.
# backtracking

import sys
sys.stdin = open('sample_input.txt')

def nPr(k, arr):                            # N 개 중 2개를 뽑아 순열 생성
    global food
    if k == 2:
        food += lst[temp[0]][temp[1]]       # 뽑은 순열로 시너지 합 저장
        return

    for i in arr:
        if i not in temp:
            temp.append(i)
            nPr(k+1, arr)
            temp.pop()

def backtracking(k, s):                     # 조합 생성, k: 인덱스, s: 시작값
    if k == N//2:                           # arr1: N개 중 N//2 개 뽑기
        total = set(range(N))
        arr2 = list(total - set(arr1))      # arr2: 선택한 경우의 여집합 생성
        ret.append((list(arr1), arr2))      # ????? 여기 왜 arr1에 list() 붙여야 될까요..???
        return

    if k != 0:
        s = arr1[-1] + 1

    for i in range(s, N):
        if i not in arr1:
            arr1.append(i)
            backtracking(k+1, s)
            arr1.pop()

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    arr1 = []
    ret = []
    backtracking(0, 0)          # N개 중 N//2개 선택

    result = []
    for arr1, arr2 in ret:      # 생성된 조합 중
        food = 0
        temp = []
        nPr(0, arr1)            # 2개를 뽑는 순열 생성하여
        food1 = food            # 시너지 합 저장

        food = 0
        temp = []
        nPr(0, arr2)            # 위와 동일
        food2 = food

        result.append(abs(food1 - food2))   # 시너지의 차가 최소 저장

    print(f'#{case} {min(result)}') # 시너지차 최소값

####################
# 2.
# itertools

import sys
sys.stdin = open('sample_input.txt')

from itertools import combinations

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    row_sum = [sum(row) for row in lst]                             # row 합
    col_sum = [sum(col) for col in zip(*lst)]                       # col 합

    sub_sum = [sum(x) for x in zip(row_sum, col_sum)]               # row + col
    total_sum = sum(row_sum)
    ret = [abs(total_sum - sum(x)) for x in combinations(sub_sum, N//2)]    # row + col 에서 2개 뽑아 더한 값 - 전체 합 = 시너지 합의 차

    print(f'#{case} {min(ret)}')