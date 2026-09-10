class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Stack - Push numbers into the stack, but pop top two numbers for operator
        # and then push the result onto the stack. Stack will always hold the 
        # intermediate results and the answer will be the remaining number on stack.
        # Time: O(n) / Space: O(n)

        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left / right))
        return stack[0]


        # # Recursion - Using DFS, perform the last operation. The operand will be
        # # returned after performing its own DFS and so forth.
        # # Time: O(n) / Space: O(n)
        # def dfs():
        #     token = tokens.pop()
        #     if token not in "+-*/":
        #         return int(token)
        #     right = dfs()
        #     left = dfs()
        #     if token == '+':
        #         return left + right
        #     elif token == '-':
        #         return left - right
        #     elif token == '*':
        #         return left * right
        #     elif token == '/':
        #         return int(left / right)
        # return dfs()


        # # Brute force - From left to right, find the first operator[s]. Perform the
        # # operation[s] on the operands behind. Keep the result in the correct index
        # # and modify the tokens list to be used in next operation.
        # # Final result should be the only token in list.
        # # Time: O(n^2) / Space: O(1)
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-*/":
        #             a = int(tokens[i - 2])
        #             b = int(tokens[i - 1])
        #             if tokens[i] == '+':
        #                 result = a + b
        #             elif tokens[i] == '-':
        #                 result = a - b
        #             elif tokens[i] == '*':
        #                 result = a * b
        #             elif tokens[i] == '/':
        #                 result = int(a / b)
        #             tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
        #             break
        # return int(tokens[0])