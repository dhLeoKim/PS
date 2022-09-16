###############
# 1
# itertools

import sys
sys.stdin = open('input.txt')

from itertools import combinations as cb

T = int(input())
for case in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ret = []
    result = []
    for i in range(1, len(lst)+1):              # 조합으로 부분 집합 생성
        temp = list(map(list, (cb(lst, i))))    

        for tower in temp:
            if sum(tower) >= B:                 # 높이가 B이상인 경우만 선택
                ret.append(sum(tower))

    print(f'#{case} {min(ret) - B}')            # 그 중 최소높이의 차 출력 

###############
# 2
# backtracking

import sys
sys.stdin = open('input.txt')

def backtracking(k, s):                 # k: 인덱스, s: 높이 합
    global cnt
    cnt += 1
    if k == N:                          # 부분 집합 생성 완료
        if s >= B:                      # 높이가 B 이상인 경우만 선택
            ret.append(s)
        return
    # prunning
    elif s >= B:                        # 가지치기
        ret.append(s)
        return
    else:                               # 부분 집합 생성 중
        backtracking(k+1, s+lst[k])     # 포함o
        backtracking(k+1, s)            # 포함x

T = int(input())
for case in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    ret = []
    backtracking(0, 0)

    print(f'#{case} {min(ret)-B}')      # 그 중 최소높이의 차 출력