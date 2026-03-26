class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 1
        m = 10
        while n >= m:
            n -= m
            m -= 1
            turn *= -1
        return turn != 1
