import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for case in range(T):
    N = list(input())
    lst = input().split()
    S = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    I = list(range(10))
    stoi = dict(zip(S, I))
    itos = dict(zip(I, S))

    for i in range(len(lst)):
        lst[i] = stoi[lst[i]]

    for i in range(len(lst)):
        lst[i] = itos[lst[i]]

    print(f'#{case+1}', *lst)