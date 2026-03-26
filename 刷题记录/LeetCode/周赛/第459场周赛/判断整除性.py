class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = 0
        y = 1
        for i in map(int, str(n)):
            x += i
            y *= i
        return n % (x + y) == 0
