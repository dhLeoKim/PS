import sys
sys.stdin = open('input_1654.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))

# 10,000 X 1,000,000 = 10,000,000,000 이기에 O(N^2)이 불가능
# 이러면 O(log(N)) 으로 찾을 수 있는 방법 생각하기
# 이분탐색!

start = 1
end = max(lst)
while start <= end:
    mid = (start+end)//2
    line_num = 0

    # mid길이로 잘리는 랜선의 개수
    for i in range(K):
        line_num += lst[i]//mid

    if line_num >= N:
        start = mid+1
    else:
        end = mid-1

print(end)