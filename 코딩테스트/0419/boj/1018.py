import sys
sys.stdin = open('input_1018.txt')
input = sys.stdin.readline

# 최악의 경우 8x8 2중 for문 확인을 42번해야함
# 64*42 -> 부루트포스로 해결 가능!
# 정해진 경우의 수가 검정 시작, 하양 시작 두가지 밖에 없음
# 시작이 검정 -> 홀수가 다 검정인지 확인
# 시작이 하양 -> 홀수가 다 하양인지 확인
# 이 때 i, j 각각 홀짝을 나누면 분기가 굉장히 복잡해짐

# 그래서 2차원 배열의 홀짝 판단 필요 
# (i+j)%2 로 홀짝 판단!

N, M = map(int, (input().split()))
lst = [list(input().strip()) for _ in range(N)]

ret = []
for si in range(N-7):
    for sj in range(M-7):
        black_start = 0
        white_start = 0

        for i in range(si, si+8):
            for j in range(sj, sj+8):
                if (i+j)%2 == 0:
                    if lst[i][j] != 'B':
                        black_start += 1
                    elif lst[i][j] != 'W':
                        white_start += 1
                else:
                    if lst[i][j] != 'W':
                        black_start += 1
                    elif lst[i][j] != 'B':
                        white_start += 1

        ret.append(black_start)
        ret.append(white_start)

print(min(ret))