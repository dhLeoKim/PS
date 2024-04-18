def solution(phone_book):
    # string이라서 정렬시 같은 숫자들 끼리 군집하여 정렬 됨
    # 따라서 탐색 효율성이 증가
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))