def is_valid(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return len(stack) == 0

def check_bracket_rotation(s):
    for i in range(len(s)):
        if is_valid(s):
            return f"짝이 맞았습니다! 괄호를 {i}번 이동했습니다."
        # 앞 문자 하나를 뒤로 이동
        s = s[1:] + s[0]
    return "올바른 배열이 아닙니다"

# ✅ 사용 예시
input_str = "}]()[{"
print(check_bracket_rotation(input_str))
