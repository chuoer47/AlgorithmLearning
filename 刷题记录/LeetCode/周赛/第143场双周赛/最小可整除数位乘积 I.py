class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(x):
            x = list(map(int,str(x)))
            ans = 1
            for i in x:
                ans *= i
            return ans%t==0
        x = n
        while True:
            if check(x):
                return x
            x += 1
        return -1