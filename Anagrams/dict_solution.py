"""
This is a more efficient solution than the sorting solution.

The time complexity should be O(n).
"""


def is_annagram(s1, s2):
    s1_dict = _count_letters(s1)
    s2_dict = _count_letters(s2)

    if len(s1_dict.keys()) != len(s2_dict.keys()):
        return False

    for letter, count in s1_dict.items():
        if letter not in s2_dict or s2_dict[letter] != count:
            return False

    return True


def _count_letters(s):
    counts = dict()
    for l in s:
        if l in counts.keys():
            counts[l] += 1
        else:
            counts[l] = 1

    return counts
