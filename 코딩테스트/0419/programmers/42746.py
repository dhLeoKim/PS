def solution(numbers):

    numbers_str = []
    for number in numbers:
        numbers_str.append(str(number))
    
    # 34, 3, 30 순서로 정렬하기 위해서 lambda x:x*3
    # 이러면 343434, 333, 303030 에서 343, 333, 303 으로 비교하게됨
    # 문제조건에서 numbers의 값이 0 이상 1000 이하 이기에
    # 최소값을 기준으로 3자리 수를 만들기 위해 x*3
    numbers_str.sort(reverse=True, key=lambda x:x*3)
    
    ret = ''
    for number in numbers_str:
        ret += number
    
    # "000"과 같은 값을 "0"으로 바꾸기 위해 int변환후 다시 str변환
    return str(int(ret))

numbers = [10, 0, 0]

print(solution(numbers))