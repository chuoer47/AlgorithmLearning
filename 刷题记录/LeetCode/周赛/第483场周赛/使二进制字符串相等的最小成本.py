class Solution:
    def minimumCost(
        self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int
    ) -> int:
        # 应该是贪心，但是是比较难想的
        # 首先分类两种情况，如果 2*filpCost <= swapCost/crossCost，那就只用filpCost就可以了
        # 但是如果 2*filpCost > swapCost/crossCost，要分类讨论一下swapCost/crossCost之间的关系
        # 如果swapCost <= crossCost，优先把
        cnt0 = cnt1 = 0
        for x, y in zip(s, t):
            if x == y:
                continue
            if x == "0":
                cnt0 += 1
            else:
                cnt1 += 1
        if 2 * flipCost <= swapCost:
            return flipCost * (cnt0 + cnt1)
        mn = min(cnt0, cnt1)
        ans = swapCost * mn
        cnt = max(cnt0, cnt1) - mn
        cost = min(swapCost + crossCost, 2 * flipCost)
        ans += (cnt // 2) * cost + (cnt % 2) * flipCost
        return ans