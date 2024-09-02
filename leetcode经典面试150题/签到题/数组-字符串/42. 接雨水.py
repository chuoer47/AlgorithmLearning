from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i, v in enumerate(height):
            while stack and height[stack[-1]] <= v:
                bottom_h = height[stack.pop()]
                if not stack:
                    break
                l, r = stack[-1], i
                h = min(height[l], v) - bottom_h
                ans += h * (r - l - 1)
            stack.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
