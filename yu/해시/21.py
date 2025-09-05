def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):                 #원하는 품목  딕셔너리 생성
        want_dict[want[i]] = number[i]

    answer = 0

    for i in range(len(discount) - 9):
        discount_10d = {}                      #할인품목이 원하는 품목 딕셔너리에 있으면 10일 할인품목 딕셔너리에 각 품목별 개수 저장
        for j in range(i, i + 10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1

        print(f"Day {i}: {discount[i:i+10]} ->", discount_10d)

        match = True 
        for item in want_dict:                                  #할인품목 딕셔너리에 원하는 품목이 있으면 기존키 없으면 0반환 
            if discount_10d.get(item, 0) < want_dict[item]:     #할인품목에 내가 원하는 품목이 있으면 할인품목개수 반환 후 
                match = False                                   #내가 원하는 품목개수보다 할인품목개수가 작으면 False  반환
                break
        
        if match:
            print("매칭성공 at day", i)
            answer += 1

    return answer





# 예시 데이터
want = ["apple", "banana"]
number = [2, 1]
discount = [
    "apple", "banana", "apple", "milk", "bread",
    "apple", "banana", "apple", "banana", "apple",
    "banana", "apple", "banana", "apple", "milk"
]

print("최종 매칭 개수:", solution(want, number, discount))
