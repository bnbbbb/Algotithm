import re
from itertools import permutations
def solution(expression):
    def calculate(operators, operand):
        for operator in operators:
            i = 0
            while i < len(operand):
                if operand[i] == operator:
                    result = eval("".join(operand[i-1:i+2]))
                    operand[i-1:i+2] = [str(result)]
                else:
                    i += 1
        return int(operand[0])
    answer = 0
    operators  = ['*', '+', '-']
    operator_permutations = list(permutations(operators))
    exp = re.findall( r'\d+|[-+*]', expression)

    for perm in operator_permutations:
        operand = exp[:]
        result = calculate(perm, operand)
        answer = max(answer, abs(result))

    return answer