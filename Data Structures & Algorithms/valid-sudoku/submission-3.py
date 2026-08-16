class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use a set each for rows, cols, and 3x3 boxes. 
        # Then validate the whole board in one pass.
        # Time: O(n^2) -> O(9^2) -> O(1) / Space: O(3n) -> O(27) -> O(1)
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit in rows[row] or \
                   digit in cols[col] or \
                   digit in boxes[(row // 3, col // 3)]:
                   return False
                if digit != ".":
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[(row // 3, col // 3)].add(digit)
        return True


        # # Brute force - scan each row, each col, and each 3x3 box for duplicate digits.
        # # Use a set to keep track if a digit has been encountered.
        # # Time: O(n^2) -> O(9^2) -> O(1) / Space: O(n) -> O(9) -> O(1)
        # for row in range(9):
        #     digit_set = set()
        #     for i in range(9):
        #         digit = board[row][i]
        #         if digit in digit_set:
        #             return False
        #         if digit != ".":
        #             digit_set.add(digit)
        # for col in range(9):
        #     digit_set = set()
        #     for i in range(9):
        #         digit = board[i][col]
        #         if digit in digit_set:
        #             return False
        #         if digit != ".":
        #             digit_set.add(digit)
        # for box in range(9):
        #     digit_set = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (box // 3) * 3 + i
        #             col = (box % 3) * 3 + j
        #             digit = board[row][col]
        #             if digit in digit_set:
        #                 return False
        #             if digit != ".":
        #                 digit_set.add(digit)
        # return True