from collections import deque
from utils.io_util import read_file

equations = read_file('inputs/day18.txt')

def solve(eq):
    if '(' not in eq:
        return solve_simple(eq)

    while '(' in eq:
        n_left, n_right = 1, 0
        left = eq.find('(')
        for i in range(left+1, len(eq)):
            if eq[i] == '(':
                n_left += 1
            elif eq[i] == ')':
                n_right += 1
                if n_left == n_right:
                    eq_reduced = eq[left+1 : i]
                    res = solve(eq_reduced)
                    eq = eq[:left] + str(res) + eq[i+1:]
                    break
    
    return solve_simple(eq)


def solve_simple(equation):
    """Solve equation with no parenthesis"""
    assert '(' not in equation and ')' not in equation
    eq = equation.split(' ')

    op_queue = deque()
    val_queue = deque()

    for x in eq:
        if x == '+':
            op_queue.appendleft('+')
        elif x == '*':
            while len(op_queue)> 0 and op_queue[0] == '+':
                op_queue.popleft()
                a = val_queue.popleft()
                b = val_queue.popleft()
                val_queue.appendleft(a + b)
            op_queue.appendleft('*')
        else:
            val_queue.appendleft(int(x))
    

    while len(val_queue) > 1:
        op = op_queue.popleft()
        a = val_queue.popleft()
        b = val_queue.popleft()

        if op == '+':
            val_queue.appendleft(a + b)
        else:
            val_queue.appendleft(a * b)
    
    return val_queue.popleft()

# equations = ['1 + 2 * 3 + 4 * 5 + 6',
#      '2 * 3 + (4 * 5)',
#      '5 + (8 * 3 + 9 + 3 * 4 * 3)',
#      '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
#      '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']

res = 0
for equation in equations:
    # print(solve(equation))
    res += solve(equation)

print(res)