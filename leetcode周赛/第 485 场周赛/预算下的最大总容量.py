max = lambda x,y:x if x > y else y

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        # 选 cost+cap1 ，去找最大为 budge-1-cost 能得到的最大的容量
        # 维护一个单调栈
        item = sorted([[x, y] for x, y in zip(costs, capacity)])
        st1, st2 = [0], [0]
        ans = 0
        for x, y in item:
            if x >= budget:
                break
            idx = bisect_right(st1, budget - 1 - x) - 1
            ans = max(ans,y + st2[idx] if idx != -1 else y)
            if st2[-1] < y:
                st1.append(x)
                st2.append(y)

        return ans