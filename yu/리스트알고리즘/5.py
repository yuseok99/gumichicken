def solution(arr1, arr2):  # 함수 정의
  
  r1, c1 = len(arr1), len(arr1[0])   # r1은 행렬의 행 수 c1은 열 수
  r2, c2 = len(arr2), len(arr2[0])
  
 
  ret = [[0] * c2 for _ in range(r1)] # 행렬의 곱 결과를 담을 행렬 생성
                                      # r1,c1 x r2,c2 곱하면 행렬크기 r1,c2행렬 생성
                                      # 그리고 0으로 채워진 2차원 리스트 생성

  for i in range(r1):                 
    for j in range(c2):
     
      for k in range(c1):
        ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret