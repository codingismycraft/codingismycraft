"""Implements a trivial expression evaluator."""

def trivial_evaluator(expression):
    """Trivial expression evaluator.

    :param str expression: The expression to evaluate.

    - Each sub-expression must be enclosed in parenthesis.
    - An "operand" must be a single numeric digit.

    :returns: The evaluation of the passed in expression.
    :rtype: float.
    """
    operands = []
    operators = []
    for c in expression:
        if c == ' ' or c == '(':
            continue
        elif c in '0123456789':
            operands.insert(0, int(c))
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
    return operands.pop(0)


testing_data = [
    ["((2  * 3) + 2)", 8],
    ["((2  * 3) + (8/2))", 10],
    ["((2  + 3) + ((8/2) / 2) )", 7]
]

for expression, expected_value in testing_data:
    print(trivial_evaluator(expression))
    assert expected_value == trivial_evaluator(expression)
