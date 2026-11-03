class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Sliding Window (Optimal) - instead of fixing all unique chars in string for the
        # valid window, we depend on the maximum frequency of chars because the chars that
        # aren't the most frequent are the ones we need to replace. 
        # The window is valid while: window size - count of max freq char <= k
        # While expanding window, track freq of each char and the max freq.
        # If window size exceeds max freq, shrink it from left.
        # Time: O(n) / Space: O(n)

        freq_count = {}
        res = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            freq_count[char] = 1 + freq_count.get(char, 0)
            max_freq = max(max_freq, freq_count[char])

            while (right - left + 1) - max_freq > k:
                freq_count[s[left]] -= 1
                left += 1            
            res = max(res, right - left + 1)
    
        return res


        # Sliding Window - have left and right pointers be the window
        # Put all unique characters in a set. For each 'char', set a window that increases
        # right. Increase 'count' when right pointer is 'char'. However, if the window
        # needs more than k replacements, increase left pointer and adjust 'count'.
        # Save the maximum window size. 
        # Time: O(n^2) where n is length of string / Space: O(n)

        # res = 0
        # char_set = set(s)
        # for char in char_set:
        #     count = 0
        #     left = 0
        #     for right in range(len(s)):
        #         if s[right] == char:
        #             count += 1
        #         while (right - left + 1) - count > k:
        #             if s[left] == char:
        #                 count -= 1
        #             left += 1
        #         res = max(res, right - left + 1)
        # return res