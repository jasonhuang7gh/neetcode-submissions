class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # i is the lower boundary, j is the upper boundary
        # at the start, i is the first element and j is the last
        i, j = 0, len(nums) - 1

        while(i <= j):
            k = (i + j) // 2
            # if the midpoint is the target, index has been found
            if target == nums[k]:
                return k
            # if target in upper half, set i as midpoint (non-inclusive)
            elif nums[k] < target:
                i = k + 1
            # if target in lower half, set j as midpoint (non-inclusive)
            else:
                j = k - 1
            
        # after binary search of whole array, target is not found
        return -1