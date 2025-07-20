from typing import List


def helper(x):
    if x == 1:
        return 0
    ans = 0
    while x != 1:
        x = bin(x).count('1')
        ans += 1
    return ans


# 模板
MX = 50


class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.counts = [0] * (MX + 1)


def build_tree(depths, l, r):
    node = SegmentTreeNode(l, r)
    if l == r:
        d = depths[l]
        if d != -1 and d <= MX:
            node.counts[d] = 1
        return node
    mid = (l + r) // 2
    node.left = build_tree(depths, l, mid)
    node.right = build_tree(depths, mid + 1, r)
    # 合并左右子节点的计数
    for k in range(MX + 1):
        node.counts[k] = node.left.counts[k] + node.right.counts[k]
    return node


def update_tree(node, idx, old_d, new_d):
    if node.l == node.r == idx:
        # 更新叶子节点
        if old_d != -1 and old_d <= MX:
            node.counts[old_d] -= 1
        if new_d != -1 and new_d <= MX:
            node.counts[new_d] += 1
        return
    mid = (node.l + node.r) // 2
    if idx <= mid:
        update_tree(node.left, idx, old_d, new_d)
    else:
        update_tree(node.right, idx, old_d, new_d)
    # 更新当前节点的计数
    if old_d != -1 and old_d <= MX:
        node.counts[old_d] -= 1
    if new_d != -1 and new_d <= MX:
        node.counts[new_d] += 1


def query_tree(node, l, r, k):
    if node.r < l or node.l > r:
        return 0
    if l <= node.l and node.r <= r:
        return node.counts[k] if 0 <= k <= MX else 0
    return query_tree(node.left, l, r, k) + query_tree(node.right, l, r, k)


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 这和数位DP没啥关系
        # 我服气了，区间修改 + 区间查找...

        n = len(nums)
        depths = [helper(x) for x in nums]
        root = build_tree(depths, 0, n - 1)

        answer = []
        for query in queries:
            if query[0] == 1:
                l, r, k = query[1:]
                res = query_tree(root, l, r, k)
                answer.append(res)
            else:
                idx, val = query[1:]
                pre = depths[idx]
                now = helper(val)
                depths[idx] = now
                update_tree(root, idx, pre, now)
        return answer


if __name__ == '__main__':
    S = Solution()
    print(S.popcountDepth(nums=[3, 5, 6], queries=[[1, 0, 2, 2], [2, 1, 4], [1, 1, 2, 1], [1, 0, 1, 0]]))
