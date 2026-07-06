class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # edge case: target is smallest or largest num
        i, j = 0, len(nums) - 1
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j

        # otherwise target is somewhere in the middle
        while(j - i > 1):
            k = int((i + j) / 2)
            # if target in upper half, set i as midpoint
            if nums[k] < target:
                i = k
            # if target in lower half, set j as midpoint
            elif nums[k] > target:
                j = k
            # otherwise target is the midpoint
            else:
                return k
            
        # after binary search of whole array, target is not found
        return -1