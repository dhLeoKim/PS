import sys
sys.stdin = open('input_1231.txt')
input = sys.stdin.readline

def inorder(n):
    if n:
        inorder(ch1[n])
        print(table[n], end='')
        inorder(ch2[n])

T = 10
for case in range(1, T+1):
    N = int(input())

    table = {}
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for _ in range(N):
        temp = list(input().split())            

        table[int(temp[0])] = temp[1]

        if len(temp) > 2:
            ch1[int(temp[0])] = int(temp[2])
            if len(temp) == 4:
                ch2[int(temp[0])] = int(temp[3])

    print(f'#{case}', end=' ')
    inorder(1)
    print()