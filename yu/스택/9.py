def solution(N):
    stack = []
    while N > 0:
        a = N%2
        stack.append(str(a))
        N //=2  #몫만 남기는 코드
    binary=""   #문자열 생성하는 코드 지금은 빈문장
    while stack: #스택이 있는동안 계속 실행
        binary += stack.pop() #스택에서 꺼내서 바이너리 문장에 추가

    return binary
