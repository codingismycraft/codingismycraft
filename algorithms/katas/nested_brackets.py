def check_expression(exrp):
    open_chars = "{(["
    closing_chars = "})]"

    stack = []
    for char in exrp:
        if char in open_chars:
            stack.append(char)
        elif char in closing_chars:
            index = closing_chars.index(char)
            expected = open_chars[index]
            if not stack or stack.pop() != expected:
                return False
    return len(stack) == 0

assert check_expression("({})")
assert check_expression("")
assert check_expression("{}")
assert check_expression("{{()}}")

assert not check_expression("{})")
assert not check_expression("[]{}(")




