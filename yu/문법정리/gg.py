## 리스트 문법 (리스트는 수정가능함)
#  s=[1,2,3,4]

# .upper()  문자열을 대문자로 변경
# .lower()  문자열을 소문자로 변경
# s[n:m]    문자열을 n부터 m-1까지 꺼냄

# .append(4)  리스트뒤에다가 데이터4 추가
# .pop()      리스트 맨뒤 데이터 삭제

## 튜플 (수정이 불가능한 리스트)
#  s=(1,2,3,4)

## 세트 : 중복 X, 순서 X
#  s={1,2,3,2}
#  s.add(4)    # s = {1,2,3,4}
#  s.remove(2) # s = {1,3,4}

## 딕셔너리 키-값 저장
#  d = {'a' : 1, 'b' : 2}
#  d['a'] = 1
#  d['c'] = 3   # {'a':1, 'b':2, 'c':3}
# discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1   #.get discount[j] 가 있으면 기존 키반환 없으면 0반환 +1을 하는 이유는 기존키가 0이라서 새로나오면 +1을 해줘야하기때문


## 스택 맨뒤에 넣은 데이터 먼저 나옴 LIFO
# stack= []
# stack.append(1) 맨뒤에 1추가
# stack.pop() 맨뒤 데이터 삭제

## 큐 먼저 넣은 데이터 먼저 나옴 FIFO
# collections.deque 추천 데이터를 양쪽으로 넣고 뺄 수 있는 자료구조
# collecrions.deque를 안하고 데이터를 앞부터 제거할려면
# queue.pop(0) 을 해야되는데 매우 비효율적
# queue = deque([1,2,3])  # 덱 생성
# queue.popleft() #맨앞요소 제거
# queue.appendleft(0) #맨앞에 데이터0 추가
# queue.extend([4, 5]) #맨뒤에 데이터 4,5 추가
# queue.extendleft([0, -1]) #맨앞에 데이터 0,-1 추가 그런데 0부터 추가되어 데이터상 -1,0,1,2,3,4 이렇게됨
# queue.rotate(1) #오른쪽으로 1칸이동 (회전)




## 문법

# [표현식 for 변수 in 반복가능한객체]          반복가능한 객체에서 하나씩 꺼낸 데이터를 표현식에 맞게 변형하여 저장
# [표현식 for 변수 in 반복가능한객체 if 조건]  반복가능한 객체에서 조건에 맞는 데이터를 꺼내 표현식에 맞게 변형하여 저장 
   #<<먼저 True로 설정후 False로 되는 조건문 만들기>>
    # match = True 
    #     for item in want_dict:                                  #할인품목 딕셔너리에 원하는 품목이 있으면 기존키 없으면 0반환 
    #         if discount_10d.get(item, 0) < want_dict[item]:     #할인품목에 내가 원하는 품목이 있으면 할인품목개수 반환 후 
    #             match = False                                   #내가 원하는 품목개수보다 할인품목개수가 작으면 False  반환
    #             break
        
    #     if match:
    #         print("매칭성공 at day", i)
    #         answer += 1


# .split(" ") 띄어쓰기 기준으로 명령어 분리 하는 명령어
# .items() 딕셔너리의 (키, 값)쌍을 튜플 형태로 꺼내줍니다.
# sorted_genres = sorted(play_dict.items(), key = lambda x: x[1], reverse=True) True>내림차순정렬 sorted:정렬해서 새 리스트로 반환 key = 정렬기준 lamda x = ("pop", 100)같은 튜플 한 개 x[1]은 튜플의 두번째 값
# sorted(genres_dict[genre], key =lambda x: (-x[1], x[0])) 먼저 -x[1]으로 내림차순 정렬 후 재생횟수가 같으면 x[0]으로 오름차순 정렬


# "".join(m) m안에 있는 문자열들을 사이에 ""넣고 하나로 합침 > 'a' , 'b' >> 'ab'