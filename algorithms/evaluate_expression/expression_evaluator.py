def get_tokens(expression):
    expression = expression.replace(' ', '')
    index = 0
    operand = ''
    while index < len(expression):
        c = expression[index]
        if c == '(':
            yield c
        elif c in '0123456789.':
            operand += c
        elif c in "*+/-":
            if operand:
                yield operand
            operand = ''
            yield c
        elif c == ')':
            if operand:
                yield operand
            operand = ''
            yield c
        index += 1


def evaluator(expression):
    """Trivial expression evaluator.

    :param str expression: The expression to evaluate.

    - Each sub-expression must be enclosed in parenthesis.
    - An "operand" must be a single numeric digit.

    :returns: The evaluation of the passed in expression.
    :rtype: float.
    """
    operands = []
    operators = []
    for c in get_tokens(expression):
        if c == ' ' or c == '(':
            continue
        elif c in "*+/-":
            operators.insert(0, c)
        elif c == ')':
            op = operators.pop(0)
            v2 = operands.pop(0)
            v1 = operands.pop(0)
            new_value = None
            if op == '+':
                new_value = v2 + v1
            elif op == '-':
                new_value = v2 - v1
            elif op == '*':
                new_value = v2 * v1
            elif op == '/':
                new_value = v1 / v2
            assert new_value
            operands.insert(0, new_value)
        else:
            operands.insert(0, float(c))
    return operands.pop(0)


testing_data = [
    ["((2  * 3) + 2)", 8],
    ["((2  * 3) + (8/2))", 10],
    ["((2  + 3) + ((8/2) / 2) )", 7],
    ["((12  + 233) + ((368/4) / 2) )", 291],
    ["(12.3 * 6.2)", 76.26],
]

for expression, expected_value in testing_data:
    print(evaluator(expression))
    assert expected_value == evaluator(expression)
