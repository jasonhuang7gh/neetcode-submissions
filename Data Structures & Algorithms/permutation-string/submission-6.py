class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Sliding Window - maintain a window of k letters in s2 and its frequency
        # count. Move the window and update the count when the left char is removed
        # and the right char is added. If frequency count matches s1, return True.
        # Time: O(n) / Space: O(1)

        if len(s1) > len(s2):
            return False

        freqs_s1, freqs_s2 = [0] * 26, [0] * 26
        k = len(s1)
        for i in range(k):
            freqs_s1[ord(s1[i]) - ord('a')] += 1
            freqs_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if freqs_s1[i] == freqs_s2[i]:
                matches += 1

        left = 0
        for right in range(k, len(s2)):
            if matches == 26:
                return True

            right_char = ord(s2[right]) - ord('a')
            freqs_s2[right_char] += 1
            # new match in char count
            if freqs_s2[right_char] == freqs_s1[right_char]:
                matches += 1
            # char count matched before adding right char
            elif freqs_s2[right_char] - 1 == freqs_s1[right_char]:
                matches -= 1

            left_char = ord(s2[left]) - ord('a')
            freqs_s2[left_char] -= 1
            # new match in char count
            if freqs_s2[left_char] == freqs_s1[left_char]:
                matches += 1
            # char count matched before removing left char
            elif freqs_s2[left_char] + 1 == freqs_s1[left_char]:
                matches -= 1
            left += 1

        return matches == 26


        # # Keep a frequency map of chars in s1. For every k letters in s2, if
        # # the count of a char is exceeded, we can stop counting early and proceed
        # # to next k letters.
        # # Time: O(n * k) / Space: O(k)
        # freqs_s1 = {}
        # for char in s1:
        #     if char in freqs_s1:
        #         freqs_s1[char] += 1
        #     else:
        #         freqs_s1[char] = 1
        # k = len(s1)
        # for i in range(len(s2) - k + 1):
        #     if s2[i] in freqs_s1:
        #         freqs_s2 = {}
        #         length_s2 = 0
        #         for j in range(i, i + k):
        #             char = s2[j]
        #             if char not in freqs_s1:
        #                 break
        #             if char in freqs_s2:
        #                 freqs_s2[char] += 1
        #             else:
        #                 freqs_s2[char] = 1
        #             if freqs_s2[char] > freqs_s1[char]:
        #                 break
        #             length_s2 += 1
        #             if length_s2 == k:
        #                 return True
        # return False


        # # s1 has k letters. For every k letters in s2, compare sorted(s1) to
        # # sorted(s2 substring) and if equal, a permutation of s1 exists in s2.
        # # Time: O(n * klog(k)) / Space: O(k)
        # k = len(s1)
        # s1_sorted = sorted(s1)
        # for i in range(len(s2) - k + 1):
        #     # Slight optimization to perform comparison only if s2[i] in s1
        #     if s2[i] in s1:
        #         s2_substring = s2[i : i + k]
        #         if s1_sorted == sorted(s2_substring):
        #             return True
        # return False