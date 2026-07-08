class Solution:
    def isHappy(self, n: int) -> bool:
        cyclical_set = set()
        while(n not in cyclical_set):
            cyclical_set.add(n)
            s = str(n)
            n = 0
            for digit in s:
                n += int(digit)**2
            if n == 1:
                return True
        
        return False