class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        next_pi = list(accumulate(nextCost, initial=0))
        pre_pi = list(accumulate(previousCost, initial=0))

        def cal(n, m):
            # 向前和向后
            n, m = ord(n) - ord('a'), ord(m) - ord('a')
            if n == m:
                return 0
            if n < m:
                nxt_cost = next_pi[m] - next_pi[n]
                pre_cost = pre_pi[-1] - (pre_pi[m + 1] - pre_pi[n + 1])
                return min(nxt_cost, pre_cost)
            # n > m
            nxt_cost = next_pi[-1] - (next_pi[n] - next_pi[m])
            pre_cost = pre_pi[n + 1] - pre_pi[m + 1]
            return min(nxt_cost, pre_cost)

        return sum(cal(n, m) for n, m in zip(s, t))
