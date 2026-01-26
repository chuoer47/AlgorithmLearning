class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        st = [x for x in nums if x >= 0]
        if not st:
            return nums
        k = k % len(st)
        st = st[k:] + st[:k]
        st = st[::-1]
        for i, x in enumerate(nums):
            if x >= 0:
                nums[i] = st.pop()
        return nums