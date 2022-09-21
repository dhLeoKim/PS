def selectionSort(k, lst):
    if k == N-1:
        return

    min_idx = k
    for i in range(k, N):
        if lst[i] < lst[min_idx]:
            min_idx = i
    
    lst[k], lst[min_idx] = lst[min_idx], lst[k]

    selectionSort(k+1, lst)

lst = [2, 4, 6, 1, 9, 8, 7, 0]
N = len(lst)
selectionSort(0, lst)
print(lst)