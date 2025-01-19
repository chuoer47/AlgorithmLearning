def contibute(nums: List[int], k: int):
    # 使用单调栈完成对每个元素最小值的贡献？
    n = len(nums)
    # 左边界 left[i] 为左侧严格小于 nums[i] 的最近元素位置（不存在时为 -1）
    left = [-1] * n
    # 右边界 right[i] 为右侧小于等于 nums[i] 的最近元素位置（不存在时为 n）
    right = [n] * n
    st = []
    for i, x in enumerate(nums):
        while st and x <= nums[st[-1]]:
            right[st.pop()] = i
        if st:
            left[i] = st[-1]
        st.append(i)
    ans = 0
    for i, (x, l, r) in enumerate(zip(nums, left, right)):
        if r - l - 1 <= k:
            cnt = (i - l) * (r - i)
            ans += x * cnt
        else:
            l = max(l, i - k)
            r = min(r, i + k)
            cnt = (r - i) * (i - (r - k))
            cnt2 = (l + r + k - i * 2 + 1) * (r - l - k) // 2
            ans += x * (cnt + cnt2)
    return ans


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        ans += contibute(nums, k)
        ans -= contibute([-i for i in nums], k)
        return ans
