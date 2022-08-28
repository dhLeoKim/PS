import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    student = list(range(1, N+1))

    ret = list(set(student) - set(lst))
    ret.sort()
    
    print(f'#{case+1}', *ret)