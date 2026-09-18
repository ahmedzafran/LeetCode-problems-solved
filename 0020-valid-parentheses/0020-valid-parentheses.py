class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                try:
                    match stack[-1]:
                        case n if n == '[' and c == ']':
                            stack.pop(-1)
                        case n if n == '(' and c == ')':
                            stack.pop(-1)
                        case n if n == '{' and c == '}':
                            stack.pop(-1)
                        case _:
                            return False
                except IndexError:
                    return False
        return len(stack) == 0