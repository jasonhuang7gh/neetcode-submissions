class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use hashmap to store the complement of numbers
        # Time: O(n) / Space: O(n)
        comp_dict = {}
        for i in range(len(numbers)):
            if numbers[i] not in comp_dict:
                comp_dict[target - numbers[i]] = i
            else:
                # question assumes a 1-indexed array
                return [comp_dict[numbers[i]] + 1, i + 1]
        
        # this return is unnecessary because question states there is a valid solution
        return [0, 0]

        # # Use two pointers starting from ends to the middle
        # # Time: O(n) / Space: O(1)
        # i, j = 0, len(numbers) - 1
        # while numbers[i] + numbers[j] != target:
        #     # Compare absolute difference to see which pointer to move closer to middle
        #     if abs(numbers[i] + numbers[j - 1] - target) < \
        #        abs(numbers[i + 1] + numbers[j] - target):
        #        j = j - 1
        #     else:
        #         i = i + 1

        # # question assumes a 1-indexed array, so [0, 1] -> [1, 2]
        # return [i + 1, j + 1]