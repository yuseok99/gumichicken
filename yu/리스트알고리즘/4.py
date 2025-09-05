def solution(answers):      #함수정의
 
  patterns = [              #수포자들 패턴 정의      
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ] 
                            #수포자들의 점수 저장 리스트
  scores = [0] * 3     
  # enumrate : 인덱스i와 answer을 같이 가져옴 
  #       

  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      #i%len(pattern) > 인덱스를 패턴으로 나눈 나머지를 인덱스로 사용 
      if answer == pattern[i % len(pattern)]:
        scores[j] += 1  
 
  max_score = max(scores)     #가장 높은 점수 정의
 
  highest_scores = [ ]        #가장 높은 점수 저장 리스트
  for i, score in enumerate(scores):  #인덱스와 점수를 같이 가져옴 
    if score == max_score:            #점수가 가장높은 점수와 같다면 
      highest_scores.append(i + 1)    #가장높은 점수 리스트에 추가
  return highest_scores               