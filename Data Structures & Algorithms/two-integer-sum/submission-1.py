class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return [nums_dict[target - nums[i]], i]
            else:
                nums_dict[nums[i]] = i
        
        return [-1, -1]