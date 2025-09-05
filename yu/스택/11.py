#연속된 문자가 같으면 제거 제거하면 제거한걸로 다시 실행 
def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack)
