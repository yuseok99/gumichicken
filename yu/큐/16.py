
#뒤의 기능은 앞의 기능이 배포될 때 함께 배포되어야 합니다.
#배포 순서대로 작업 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌
# 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 반환하도록 

    #기능 퍼센트 에서 한번 100넘어 갈때까지 while실행 100넘어갈때 배포하는데 
    #뒤에 꺼도 100넘었으면 같이 배포 
    #progresses랑 speeds를 딕셔너리 
def solutions(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] >=100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        if count > 0:
            answer.append(count)

    return answer



print(solutions([93, 30, 55], [1, 30, 5]))

