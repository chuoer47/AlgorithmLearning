class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        rpi = 1
        r = n
        l = 0
        for i, x in enumerate(nums):
            while r <= i:
                rpi //= nums[r]
                r += 1
            while n >= r > i + 1 and rpi <= l:
                print(i, r, rpi, l)
                r -= 1
                rpi *= nums[r]
            if r == i + 1 and l == rpi:
                return i
            l += x
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.smallestBalancedIndex([2,8,2,2,5]))
