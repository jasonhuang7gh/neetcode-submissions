class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}
        for letter in s:
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
        
        for letter in t:
            if letter not in freq_dict:
                return False
            else:
                freq_dict[letter] -= 1
                if freq_dict[letter] == 0:
                    freq_dict.pop(letter)
        
        return len(freq_dict) == 0