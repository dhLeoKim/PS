# 1. .lower()
# 2. for 문 돌려서 제거
# 3. .replace 또는 stack 해결
# 4. .strip
# 5. .isspace 또는 '' 또는 len()
# 6. len >= 16, slicing 후 끝의 .제거
# 7. len <= 2, len() 3까지 [-1] 추가 반복

def solution(new_id):
    
    char = ['-', '_', '.']                  # 가능한 특수문자
    
    new_id = new_id.lower()                 # 알파벳 소문자

    # print(1, new_id)

    answer = ''                             # 가능한 문자만 남김
    for i in new_id:
        if i.isalpha() or i.isdecimal() or i in char: 
            answer += i

    # print(2, answer)

    while '..' in answer:                   # .. 중복 제거
        answer = answer.replace('..', '.')

    # print(3, answer)

    answer = answer.strip('.')              # 앞뒤 . 제거

    # print(4, answer)

    if answer == '':                        # 공백이면 a추가
        answer += 'a'

    # print(5, answer)

    n = len(answer)
    if n >= 16:                             # 길이 15까지
        answer = answer[:15]
        answer = answer.rstrip('.')         # 끝 . 제거

    # print(6, answer)

    if n <= 2:                              # 길이 3까지
        answer += answer[-1]*(3-n)          # 끝 문자 복사

    # print(7, answer)
    
    return answer

new_id = "=.="
solution(new_id)