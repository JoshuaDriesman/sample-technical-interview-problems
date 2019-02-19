import unittest

import sorting_solution
import dict_solution


class TestAnagrams(unittest.TestCase):
    def setUp(self):
        self.trueTestCases = [('', ''), ('abc', 'bca')]
        self.falseTestCases = [('a', 'bca'), ('bc', 'ba')]

    def test_sorting_solution(self):
        for s1, s2 in self.trueTestCases:
            with self.subTest({s1, s2}):
                self.assertTrue(sorting_solution.is_annagram(s1, s2))
        for s1, s2 in self.falseTestCases:
            with self.subTest({s1, s2}):
                self.assertFalse(
                    sorting_solution.is_annagram(s1, s2))

    def test_dict_solution(self):
        for s1, s2 in self.trueTestCases:
            with self.subTest({s1, s2}):
                self.assertTrue(dict_solution.is_annagram(s1, s2))
        for s1, s2 in self.falseTestCases:
            with self.subTest({s1, s2}):
                self.assertFalse(dict_solution.is_annagram(s1, s2))


if __name__ == '__main__':
    unittest.main()
