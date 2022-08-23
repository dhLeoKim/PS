import sys
sys.stdin = open('sample_input.txt')

def minSumSubset(i, j, local_sum):
    global min_sum

    if i == N or j == N:                                    # 부분집합 생성 완료
        if local_sum < min_sum: min_sum = local_sum         # 합의 최소값 저장
        return
    elif local_sum > min_sum: return                        # 진행 도중 최소값보다 크면 중단
    else:
        for j in range(N):                                  # 부분집합 생성 시작
            if visited[j] == True: continue
            visited[j] = True                               # 현재 위치 포함 표시
            minSumSubset(i+1, j, local_sum+lst[i][j])       # 포함한 다음 경우 탐색
            visited[j] = False                              # 다시 초기화

T = int(input())
for case in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 0                 # 초기값 설정
    for i in lst:
        min_sum += i[0]

    visited = [False]*N
    minSumSubset(0, 0, 0)       # minSubSubset(인덱스 i, 인덱스 j, 현재 경우에서의 부분집합 합)
    print(f'#{case+1} {min_sum}')