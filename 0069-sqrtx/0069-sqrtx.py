class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2147483648):
            if i * i == x:
                return i
            elif (i + 1) * (i + 1) > x:
                return i
