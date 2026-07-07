class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, ans = '', []
        for digit in digits:
            num += str(digit)
        num = int(num) + 1
        for digit in str(num):
            ans.append(digit)
        return ans
