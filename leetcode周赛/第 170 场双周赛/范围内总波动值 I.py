class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for x in range(num1, num2 + 1):
            x = str(x)
            if len(x) < 3:
                continue
            n = len(x)
            for i in range(1,n - 1):
                if x[i-1] < x[i] and x[i + 1] < x[i]:
                    ans += 1
                if x[i-1] > x[i] and x[i + 1] > x[i]:
                    ans += 1
        return ans