class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Brute force - use a set to find duplicate number
        # Time: O(n) / Space: O(n)

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return num
            else:
                nums_set.add(num)
        
        return -1