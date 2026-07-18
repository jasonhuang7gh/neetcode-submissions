class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if abs(numbers[i] + numbers[j - 1] - target) < \
               abs(numbers[i + 1] + numbers[j] - target):
               j = j - 1
            else:
                i = i + 1

        # question assumes a 1-indexed array, so [0, 1] -> [1, 2]
        return [i + 1, j + 1]