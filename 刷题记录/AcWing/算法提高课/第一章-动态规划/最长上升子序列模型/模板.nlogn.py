from typing import List
import bisect


def lengthOfLIS1(nums: List[int]) -> int:
    # Dynamic programming. O(n^2)
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lengthOfLIS2(nums: List[int]) -> int:
    # O(nlogn版本的，主要就是维护一个单调栈，使用二分替换)
    stack = []
    for num in nums:
        if not stack or num > stack[-1]:
            stack.append(num)
        else:
            # 替换策略，很巧妙，使用了python自带的二分库，减少自己写了hhhh
            stack[bisect.bisect_left(stack, num)] = num
    return len(stack)
