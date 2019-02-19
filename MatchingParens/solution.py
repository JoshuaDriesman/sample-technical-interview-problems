"""
This is one sample solution to the paren matching problem. See problem.md for the description of the problem
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


def print_test_result(inp, expected, output):
    """
    Prints out a preformatted string with the input, output, and expected value for a solution test.
    """
    print("The input was %s, the expected output was %s, and the actual output was %s." %
          (inp, output, expected))


print_test_result("", True, is_matching_parens(""))
print_test_result("()", True, is_matching_parens("()"))
print_test_result("[()]", True, is_matching_parens("[()]"))
print_test_result("[([])]", True, is_matching_parens("[([])]"))
print_test_result("[(])", False, is_matching_parens("[(])"))
print_test_result("[(]", False, is_matching_parens("[(]"))
