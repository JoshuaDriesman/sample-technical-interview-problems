"""
This is one sample solution to the paren matching problem. See problem.md for the description of the problem.

The run time of this solution is O(n).
"""

from queue import LifoQueue


def is_matching_parens(input):
    q = LifoQueue()

    for c in input:
        if c == '(' or c == '[':
            q.put(c)
        else:
            matching = q.get()
            if not ((c == ']' and matching == '[') or (c == ')' and matching == "(")):
                return False

    return q.empty()
