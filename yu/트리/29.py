def solution(enroll, referral, seller, amount):     #직원 추천인 딕셔너리 형성 >> 직원 : 총금액 딕셔너리 생성 >>
    parent = dict(zip(enroll, referral))
    parent["-"] = None

    total = {name: 0 for name in enroll}
    total["-"] = 0

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]
        print(f"\n판매자: {cur_name}, 판매금액: {money}")

        while money >0:
            give = money // 10
            receive = money - give
            total[cur_name] += receive
            print(f" {cur_name} 수익: {receive}, 상위로 전달: {give}")

            cur_name = parent[cur_name]
            if cur_name is None:
                break
            money = give
        
        if cur_name is None and give > 0:
            total["-"] += give
            print(f" 센터 수익: {give}")

    print("\n최종 수익:", total)
    return [total[name] for name in enroll] + [total["-"]]  # 센터 수익도 마지막에 추가
