class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for num in nums:
            if num in dup_set:
                return True
            else:
                dup_set.add(num)
        
        return False