import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N = int(input())

    for i in range(1, int(N**(1/3))+2):     # 세제곱근 값 근처 까지 탐색
        if i**3 == N:                       # 세제곱이 N이 되는 정수 반복문으로 확인
            ret = i
            break
    else:                                   # 정수가 아닌 경우
        ret = -1

    print(f'#{case} {ret}')