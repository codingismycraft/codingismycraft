

def solve(N, values, selections=None):
    selections = selections or []
    if sum(selections) == N:
        print(selections)
    elif sum(selections) <= N:
        for v in values:
            solve(N, values, selections[:] + [v])


solve(4, (1, 2))
