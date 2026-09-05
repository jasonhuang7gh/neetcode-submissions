class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Negative marking - this works because each num is between 1 and n
        # with only 1 duplicate. When passing through nums, flip the sign of 
        # the corresponding index. If a negative index is encountered, it means
        # we've visited this number before and it's the duplicate.
        # Time: O(n) / Space: O(1)
        for num in nums:
            index = abs(num) - 1    # nums in [1,n] instead of [0,n)
            if nums[index] < 0:
                return abs(num)
            else:
                nums[index] *= -1
        return -1


        # # Brute force - use a set to find duplicate number
        # # Time: O(n) / Space: O(n)
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return num
        #     else:
        #         nums_set.add(num)
        # return -1