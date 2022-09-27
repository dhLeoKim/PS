import sys
sys.stdin = open('sample_input.txt')

def quickSort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    left = []
    right = []

    for i in range(1, len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    return quickSort(left) + [pivot] + quickSort(right)

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    res = quickSort(lst)

    print(f'#{case}', res[N//2])