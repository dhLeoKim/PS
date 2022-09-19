import sys
sys.stdin = open('input_p1.txt')

T = int(input())
for case in range(T):
    num = input()

    N = len(num)
    a, b = divmod(N, 7)
    
    for k in range(a):
        temp = '0b' + num[k*7:(k+1)*7]
        print(int(temp, 2), end=' ')

    print()