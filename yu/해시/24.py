# 신고당한 횟수가 k이상인 사람 > 이용정지 > 통보 받은 사람을 신고한 유저한테 메일발송
def solution(id_list, report, k):
    reported_user = { }
    count = { }

    for r in report:
        user_id, reported_id = r.split( )
        if reported_id not in reported_user:
            reported_user[reported_id] = set()      #신고한 사람 당한 사람 나눈뒤 신고당한 기록이 없으면 세트 생성 후 
        reported_user[reported_id].add(user_id)     #신고당한사람={신고한사람} 인 집합(set)으로 저장
    
    for reported_id,  user_id_lst in reported_user.items():    # 신고당한 id, 신고한 id
        if len(user_id_lst) >=k:                               # 신고자들의 집합이 k개가 넘으면
            for uid in user_id_lst:                            
                if uid not in count:
                    count[uid] = 1                  
                else:
                    count[uid] += 1

    answer = [ ]
    for i in range(len(id_list)):
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    return answer


