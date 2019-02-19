"""
This is a concise solution to the anagrams problem, but the runtime is less than ideal. 

Assuming the sorting algorithm is efficient, this solution has a time complexity of O(n * log(n)).
"""


def is_annagram(s1, s2):
    return sorted(s1) == sorted(s2)
