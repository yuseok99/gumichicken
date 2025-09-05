from itertools import combinations            #손님이 주문했던 메뉴에서 n가지를 뽑아 메뉴 조합 구성
from collections import Counter               #각 메뉴 조합의 빈도를 세어 가장 많이 주문한 메뉴 쥬합을 가려냄

def solution(orders, course):                
    answer = []                              #최종 추천 코스 메뉴 저장 리스트
    for c in course:                    
        menu = []                               #해당 코스 길이에서 등장한 모든 메뉴 조합 저장
        for order in orders :
            comb = combinations(sorted(order), c)    #주문에서 가능한 모든 조합 생성
            menu += comb
        counter = Counter(menu)                      #각 메뉴 구성이 몇 번 주문되었는지 세어줌
        if len(counter) != 0 and max(counter.values()) != 1:    #len(counter) 메뉴조합이 존재하거나 max(counter.vlaues()) 가장 많이 나온 조합이 최소 2번이거나
            for m, cnt in counter.items():        #counter.items (조합, 주문횟수) 튜플 
                if cnt == max(counter.values()):  #가장많이 쓰인 조합을 answer에 
                    answer.append("".join(m))     # "".join(m) m안에 있는 문자열들을 사이에 ""넣고 하나로 합침 > 'a' , 'b' >> 'ab'

    return sorted(answer)
            

