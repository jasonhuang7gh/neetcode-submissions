class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Floyd's Cycle Detection - Because one number is duplicated, two indices
        # will point into the same chain, causing a cycle. Two pointers:
        # Slow pointer moves one step, fast pointer moves two steps at a time.
        # If there's a cycle, they will eventually meet. Then, start a new pointer
        # from the beginning and move it one step at a time along with the original
        # slow pointer. They will meet at the duplicate number.

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow


        # # Negative marking - this works because each num is between 1 and n
        # # When passing through nums, treat the num as an index and flip the sign of 
        # # the num at that index. If a negative index is encountered, it means
        # # we've visited this number before and it's the duplicate.
        # # Time: O(n) / Space: O(1)
        # for num in nums:
        #     index = abs(num) - 1    # nums in [1,n] instead of [0,n)
        #     if nums[index] < 0:
        #         return abs(num)
        #     else:
        #         nums[index] *= -1
        # return -1


        # # Brute force - use a set to find duplicate number
        # # Time: O(n) / Space: O(n)
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return num
        #     else:
        #         nums_set.add(num)
        # return -1