import unittest

from solution import is_matching_parens


class TestMatchingParens(unittest.TestCase):
    def test(self):
        self.assertTrue(is_matching_parens(""))
        self.assertTrue(is_matching_parens("()"))
        self.assertTrue(is_matching_parens("[()]"))
        self.assertTrue(is_matching_parens("[([])]"))
        self.assertFalse(is_matching_parens("[(])"))
        self.assertFalse(is_matching_parens("[(]"))


if __name__ == '__main__':
    unittest.main()
