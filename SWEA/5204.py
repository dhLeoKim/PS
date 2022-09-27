import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    global ret
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:     # 왼쪽이 작으면 병합배열에 왼쪽 추가
            merged.append(left[l])
            l += 1
        else:                       # 오른쪽이 작으면 병합배열에 오른쪽 추가
            merged.append(right[r])
            r += 1

    merged += left[l:]              # 마지막으로 남은 원소 추가
    merged += right[r:]             # [:] slicing으로 작성시 index error 발생 안함!!!

    if r == len(right):             # 문제에서 요구하는 케이스일 경우 +1
        ret += 1

    return merged

def mergeSort(lst):
    if len(lst) <= 1:               # 원소가 1개가 될 때까지
        return lst

    m = len(lst)//2                 # 중앙을 기준으로 분할
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])

    return merge(left, right)       # 병합

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ret = 0
    res = mergeSort(lst)
    print(f'#{case}', res[N//2], ret)