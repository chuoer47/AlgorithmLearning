class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        def helper(flag):
            cnt = 0
            mx_v, mn_v = -inf, inf
            mx_nv, mn_nv = -inf, inf
            for x in nums:
                if x % 2 == flag:
                    mx_nv = max(mx_nv, x)
                    mn_nv = min(mn_nv, x)
                else:
                    cnt += 1
                    mx_v = max(mx_v, x)
                    mn_v = min(mn_v, x)
                flag ^= 1
            if cnt == 0:  # 完美符合
                return 0, max(nums) - min(nums)
            if cnt == len(nums):  # 完美不符合
                return cnt,abs(mx_v - 1 - mn_v - 1)
            diff = inf
            for dx, dy in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                x = mx_v + dx
                y = mn_v + dy
                tmp = [mx_nv, mn_nv, x, y]
                diff = min(diff, max(tmp) - min(tmp))
            return cnt, diff

        cnt1, diff1 = helper(0)
        cnt2, diff2 = helper(1)

        if cnt1 < cnt2:
            return [cnt1, diff1]
        elif cnt2 < cnt1:
            return [cnt2, diff2]
        return [cnt2, min(diff1, diff2)]