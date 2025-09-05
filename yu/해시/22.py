# 1. 최종으로 구하는 것 > 최종으로 보는 메시지
# 2. 입력값 중 수정되지 않는 건 뭐지? > 유저 아이디
# 3. 입력값 중 수정되는 것 > 닉네임
# 3-1 입력값이 수정되면 영향 받는곳 > 오픈채팅방의 내용 변경
# 3-2 입력값은 Enter와 Change인 경우에 바뀜

# 1. 알맞은 자료구조 선택 
# -메시지의 변경되는 값은 닉네임 닉네임은 record에 의해 변경되며 닉네임의 식별자는 유저 id
# -따라서 유저 id의 닉네임을 바로 찾고 업데이트 할 수 있는 딕셔너리가 효율적임

def solution(record):
    answer = []
    uid = {}
    for line in record:
        cmd = line.split(" ")

        if cmd[0] != "Leave" :
            uid[cmd[1]] = cmd[2]
        
    for line in record:
        cmd = line.split(" ")

        if cmd[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
        elif cmd[0] == "Change":
            pass
        else:
            answer.append("%s님이 나갔습니다." % uid[cmd[1]])
    return answer