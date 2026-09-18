class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        input = list(x)
        input_reverse = input.copy()
        input_reverse.reverse()
        return input == input_reverse
        
        