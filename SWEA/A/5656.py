import sys
sys.stdin = open('input_5656.txt')

from itertools import product
from collections import deque

def func2():                                        ######################## 벽돌 정리 함수
    brick = 0
    for i in range(W):
        stack = []
        for j in range(H):
            if arr[i][j]:
                stack.append(arr[i][j])
                brick += 1
        stack = [0]*(H-len(stack)) + stack
        arr2.append(stack)
    
    return brick

def func(i, j, val):                                ######################## 연쇄 폭발 함수
    di, dj = [0, 1, -1, 0], [1, 0, 0, -1]
    queue = deque()
    queue.append((i, j, val))
    arr[i][j] = 0
    brick = 1
    while queue:
        i, j, val = queue.popleft()
        if val == 0:
            break
        for n in range(1, val+1):
            for k in range(4):
                ni, nj = i + di[k]*n, j + dj[k]*n
                if 0 <= ni < W and 0 <= nj < H and arr[ni][nj] != 0:
                    if arr[ni][nj] != 1:
                        queue.append((ni, nj, arr[ni][nj]-1))
                    arr[ni][nj] = 0
                    brick += 1
    return brick

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())              ######################## 입력 받기
    lst = []
    M = 0
    for _ in range(H):
        temp = list(map(int, input().split()))
        M += temp.count(0)                           # 0의 개수 세기
        lst.append(temp)

    flag = 0                                         # skip을 위한 flag
    ret = 1e9                                        # 결과값
    for case in product(range(W), repeat=N):         ######################## 중복 순열 생성
        if flag:
            idx, prev_case = prev
            if case[idx] == prev_case:               # 쏴야할 곳에 더이상 벽돌이 없는 경우 skip
                continue                             # 다음 자리 선택을 skip 하고 현재자리 +1 (가지치기)
            else:
                flag = 0
        
        arr = [list(x) for x in zip(*lst)]           # 폭발 후 벽돌 정리를 편하게 하기 위해서 전치된 배열 사용

        brick = W*H - M
        for idx in range(N):                         ######################## 벽돌에 구슬을 쏴서 폭발
            i = case[idx]
            for j in range(H):
                if arr[i][j] == 0:                   # 벽돌이 있는 경우에만 폭발 진행
                    continue
                temp = func(i, j, arr[i][j]-1)       # 폭발된 개수를 반환
                if temp == 1:                        # 시간 단축을 위한 코드
                    brick -= 1
                    break
                arr2 = []
                brick = func2()                      ######################## 폭발 후 벽돌 아래로 당겨서 정리
                arr = []
                for row in arr2:                     # 다음 폭발을 위한 깊은 복사
                    arr.append(row[:])
                break
            else:                                    # 쏴야할 곳에 더이상 벽돌이 없는 경우의 예외 처리
                flag = 1
                prev = (idx, case[idx])
                arr2 = []
                brick = func2()
                break
        
        if brick < ret:                              # 남은 벽돌 개수의 최소값
            ret = brick

    print(f'#{tc}', ret)