import unittest

from solution import is_matching_parens


class TestMatchingParens(unittest.TestCase):
    def setUp(self):
        self.trueTestCases = ["", "()", "[()]", "[([])]"]
        self.falseTestCases = ["[(])", "[(]"]

    def test(self):
        for case in self.trueTestCases:
            self.assertTrue(is_matching_parens(case))
        for case in self.falseTestCases:
            self.assertFalse(is_matching_parens(case))


if __name__ == '__main__':
    unittest.main()
