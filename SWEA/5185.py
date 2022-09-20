import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N, lst = input().split()

    num_bin = ''
    for num_hex in lst:
        temp = bin(int(num_hex, 16))[2:]
        temp = '0'*(4-len(temp)) + temp
        num_bin += temp

    print(f'#{case} {num_bin}')