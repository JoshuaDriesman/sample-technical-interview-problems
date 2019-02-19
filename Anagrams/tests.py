import unittest

import sorting_solution


class TestAnagrams(unittest.TestCase):
    def setUp(self):
        self.trueTestCases = [('', ''), ('abc', 'bca')]
        self.falseTestCases = [('a', 'bca'), ('bc', 'ba')]

    def test_sorting_solution(self):
        for case in self.trueTestCases:
            self.assertTrue(sorting_solution.is_annagram(case[0], case[1]))
        for case in self.falseTestCases:
            self.assertFalse(sorting_solution.is_annagram(case[0], case[1]))


if __name__ == '__main__':
    unittest.main()
