def solution(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[len(phone)] = phone

    phone_keys = sorted(list(phone_dict.keys()))
    print(phone_dict)
    
    # for i in phone_keys:

    
    return

phone_book = ["119", "97674223", "1195524421"]	
phone_book = ["1195524421", "97674223", "119"]	
# phone_book = ["123","456","789"]	
# phone_book = ["12","123","1235","567","88"]	

print(solution(phone_book))