def solution(N, stages):   #함수 정의  N은 스테이지수 stages는 도전중인 스테이지
 
  challenger = [0] * (N +2)  # i번째 스테이지에서 도전중인 사람수 N스테이지가 마지막인데 0부터 시작이므로 +1, 모든스테이지를 다 통과한사람은 N+1이므로 총 N+2가된다

  for stage in stages:     #도전중인 스테이지수를 기반으로 도전중인 사람수 +1
    challenger[stage] +=1  

    fails = { }            #실패율 딕셔너리사용
    total = len(stages)    #스테이지에 도전중인 총 사람수

    for i in range(1,N +1): #1부터 N까지 스테이지를 순회  range(start,end)는 start부터 end-1까지
      if challenger[i] == 0: #스테이지에 도전한 사람이 0명이면 
        fails[i] = 0         #실패율은 0
      else:                  
        fails[i] = challenger[i] / total  #실패율은 스테이지에 머무른 사람 / 총 도전자 수
        total -= challenger[i]  #전 스테이지에 머무른 사람은 다음 총 사람수에서 빼줘야되기때문에 빼준다


    result = sorted(fails, key=lambda x : fails[x], reverse=True) 
    #리스트정렬 fails딕셔너리를 key값만 빼서 리스트로 정렬 reverse=True >> 내림차순정렬 

    return result