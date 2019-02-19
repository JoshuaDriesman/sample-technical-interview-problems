"""
This is one sample solution to the paren matching problem. See problem.md for the description of the problem.

The run time of this solution is O(n).
"""


def is_matching_parens(input):
    q = list()

    for c in input:
        if c == '(' or c == '[':
            q.append(c)
        else:
            matching = q.pop()
            if not ((c == ']' and matching == '[') or (c == ')' and matching == "(")):
                return False

    return len(q) == 0
