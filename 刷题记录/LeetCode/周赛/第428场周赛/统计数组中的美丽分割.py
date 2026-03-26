mod = int(1e9 + 7)
B = 52
mx = 5000
base = [1] * (mx + 1)
for i in range(1, mx + 1):
    base[i] = base[i - 1] * B % mod


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        # 先预处理哈希
        n = len(nums)
        hval = [0] * (n + 1)
        for i, num in enumerate(nums):
            hval[i + 1] = (hval[i] * B + num + 1) % mod

        def substr(l, r):
            # [l,r] 左闭右闭的字符串
            return (hval[r + 1] - hval[l] * base[r + 1 - l]) % mod

        # 遍历
        # 0..i ; i+1..j ; j + 1....
        ans = 0
        for i in range(0, n):
            for j in range(i + 1, n - 1):
                l1, l2, l3 = i + 1, j - i, n - j - 1
                if l1 <= l2 and substr(l=0, r=i) == substr(l=i + 1, r=i + l1):
                    ans += n - j - 1
                    break
                if l2 <= l3:
                    ans += substr(l=i + 1, r=j) == substr(l=j + 1, r=j + l2)
        return ans
