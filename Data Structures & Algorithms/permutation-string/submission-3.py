class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Keep a frequency map of chars in s1. For every k letters in s2, if
        # the count of a char is exceeded, we can stop counting early and proceed
        # to next k letters.
        # WIP


        # s1 has k letters. For every k letters in s2, compare sorted(s1) to
        # sorted(s2 substring) and if equal, a permutation of s1 exists in s2.
        # Time: O(n * klog(k)) / Space: O(k)
        k = len(s1)
        s1_sorted = sorted(s1)
        for i in range(len(s2) - k + 1):
            # Slight optimization to perform comparison only if s2[i] in s1
            if s2[i] in s1:
                s2_substring = s2[i : i + k]
                if s1_sorted == sorted(s2_substring):
                    return True
        return False