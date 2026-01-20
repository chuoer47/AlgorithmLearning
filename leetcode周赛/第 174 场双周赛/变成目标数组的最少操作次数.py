class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        cnt = defaultdict(bool)
        for x, y in zip(nums, target):
            if x != y:
                cnt[x] = True
        return sum(cnt.values())
