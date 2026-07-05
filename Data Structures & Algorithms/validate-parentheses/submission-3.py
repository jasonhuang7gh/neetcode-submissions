class Solution:
    def isValid(self, s: str) -> bool:

        # Put open brackets into a stack
        # Remove if corresponding closed bracket is encountered
        bracket_dict = {')':'(', '}':'{', ']':'['}
        bracket_stack = []

        for bracket in s:
            if bracket not in bracket_dict:
                bracket_stack.append(bracket)
            else:
                # bracket_stack.pop() removes the last element and also returns it
                # if exception happens, it's because stack is empty and pop() failed
                try:
                    if bracket_dict[bracket] != bracket_stack.pop():
                        return False
                except:
                    return False
        
        return len(bracket_stack) == 0



