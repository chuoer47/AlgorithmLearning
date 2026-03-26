class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        s = sorted(set(nums))
        n = len(s)
        for i in range(n):
            for j in range(i + 1,n):
                if cnt[s[i]] != cnt[s[j]]:
                    return [s[i],s[j]]
        return [-1,-1]