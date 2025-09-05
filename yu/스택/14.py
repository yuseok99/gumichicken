#Ux 현재 선택한 행에서 x칸위에 있는 행선택
#Dx 현재 선택한 행에서 x칸 아래에 있는 행 선택
#C 현재 선택한 행 삭제후 바로 아래 행 선택 단
#  삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
#Z 가장 최근에 삭제한 행을 원래대로 복구 현재선택한 행은 안바뀜\
#정답은 표의 0행부터 n-1행까지에 해당되는 O,X를 순서대로 이어붙인 문자열 형태로 반환
def solution(n,k,cmd):

    
    deleted = []
    result = []
    
    for i in range(n):
        result.append("O")


    for cmd_i in cmd:
        if cmd_i.startswith("C"):
            deleted.append(k)
            result[k] = "X"
           
            if k != n-1 :
                k += 1
            else:
                k -= 1
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()  
            result[restore] = "O"

        elif cmd_i.startswith("U") or cmd_i.startswith("D"):
            action, num = cmd_i.split()
            num = int(num)
            if cmd_i.startswith("U"):
                if k >= num :
                    k = k - num
                elif k < num :
                    k = 0
            if cmd_i.startswith("D"):
                if k + num <= n-1 :
                    k = k + num
                elif k + num > n-1 :
                    k = n - 1
    return result


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "Z", "Z"]

print(solution(n, k, cmd))



        





        