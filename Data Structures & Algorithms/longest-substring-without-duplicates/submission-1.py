class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Use 'left' and 'right' indices to maintain a substring.
        # As substring expands by moving 'right' forward, add the char to a set.
        # If a duplicate char is encountered, move 'left' forward until there are
        # no more duplicates in substring, while removing chars from the set.
        # Time: O(n) / Space: O(n)

        left, right = 0, 0
        curr_length, longest_length = 0, 0
        char_set = set()

        while right < len(s):
            curr_right = s[right]
            if curr_right not in char_set:
                char_set.add(curr_right)
                right += 1
                curr_length += 1
            else:
                longest_length = max(longest_length, curr_length)
                while curr_right in char_set:
                    curr_left = s[left]
                    char_set.remove(curr_left)
                    left += 1
                    curr_length -= 1
        
        return max(longest_length, curr_length)