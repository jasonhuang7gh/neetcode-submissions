class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Brute force - scan each row, each col, and each 3x3 box for duplicate digits.
        # Use a set to keep track if a digit has been encountered.
        # Time: O(n^2) -> O(9^2) -> O(1) / Space: O(n) -> O(9) -> O(1)

        for row in range(9):
            digit_set = set()
            for i in range(9):
                digit = board[row][i]
                if digit in digit_set:
                    return False
                if digit != ".":
                    digit_set.add(digit)
        
        for col in range(9):
            digit_set = set()
            for i in range(9):
                digit = board[i][col]
                if digit in digit_set:
                    return False
                if digit != ".":
                    digit_set.add(digit)
        
        for box in range(9):
            digit_set = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    digit = board[row][col]
                    if digit in digit_set:
                        return False
                    if digit != ".":
                        digit_set.add(digit)
        
        return True