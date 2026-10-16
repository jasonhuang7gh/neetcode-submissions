class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Sliding Window - have left and right pointers be the window
        # Put all unique characters in a set. For each 'char', set a window that increases
        # right. Increase 'count' when right pointer is 'char'. However, if the window
        # needs more than k replacements, increase left pointer and adjust 'count'.
        # Save the maximum window size.
        # Time: O(n^2) where n is length of string / Space: O(n)

        res = 0
        char_set = set(s)

        for char in char_set:
            count = 0
            left = 0
            for right in range(len(s)):
                if s[right] == char:
                    count += 1
                
                while (right - left + 1) - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                
                res = max(res, right - left + 1)

        return res