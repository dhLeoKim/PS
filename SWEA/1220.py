import sys
sys.stdin = open('input.txt')

# 위가 N 오른쪽

# 1은 N극 빨강
# 2는 S극 파랑

# 아래가 S 왼쪽

T = 10
for case in range(T):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]

    cnt = 0
    lst = list(zip(*lst))
    for i in lst:
        i = ''.join(map(str, i))
        i = i.replace('0', '')
        i.lstrip('2')
        i.rstrip('1')
        cnt += i.count('12')

    print(f'#{case+1} {cnt}')