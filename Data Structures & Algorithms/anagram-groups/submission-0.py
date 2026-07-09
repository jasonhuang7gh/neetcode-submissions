class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for string in strs:
            s = ''.join(sorted(string)) # sorted() returns List[str]
            if s in anagram_dict:
                anagram_dict[s].append(string)
            else:
                anagram_dict[s] = [string]
        
        return list(anagram_dict.values())