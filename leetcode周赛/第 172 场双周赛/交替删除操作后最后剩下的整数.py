class Solution:
    def lastInteger(self, n: int) -> int:
        # n=1e15，绝对不可能使用模拟的方式完成
        # 应该是数学的方式完成
        # 或者logn的递归完成方式
        def helper(n, way):
            # n表示删除长度，way表示删除的操作是0还是1
            if n == 1:
                return 1
            nxt = helper((n + 1) // 2, way ^ 1)
            if way == 0:
                ans = 2 * nxt - 1
            else:
                ans = 2 * nxt - n % 2
            return ans

        return helper(n, 0)
