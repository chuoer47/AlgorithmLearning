class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        # 不会又是一个换根DP?
        # 考虑节点i为根的情况下,其他group[j]的距离记录 (长度最大为20)
        # 换子节点j,ans[root] - ans[j] + 整体+1 =>
        group = [i - 1 for i in group]
        # cnt[i][j]表示以i为根节点,j=group_id的个数
        cnt = [[0] * 20 for _ in range(n)]
        # path[i][j]表示以i为根节点,下面子树j=group_id到i的距离
        path = [[0] * 20 for _ in range(n)]
        ans = 0
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, fa):
            group_id = group[node]
            cnt[node][group_id] += 1
            for nxt in g[node]:
                if nxt == fa:
                    continue
                dfs(nxt, node)
                ch_path = path[nxt]
                ch_cnt = cnt[nxt]
                for j in range(20):
                    cnt[node][j] += ch_cnt[j]
                    path[node][j] += ch_path[j] + ch_cnt[j]

        dfs(0, -1)

        def reroot(node, fa):
            nonlocal ans
            group_id = group[node]
            ans += path[node][group_id]  # 只能添加同一组的距离
            for nxt in g[node]:
                if nxt == fa:
                    continue
                # 开始换根,需要先保留
                p_nxt_cnt = cnt[nxt].copy()
                p_nxt_path = cnt[nxt].copy()
                tmp_path = [path[node][i] - path[nxt][i] - cnt[nxt][i] for i in range(20)]  # 这个是node是nxt子节点的path的情况
                tmp_cnt = [cnt[node][i] - cnt[nxt][i] for i in range(20)]  # 这个是node是nxt子节点cnt的情况
                cnt[nxt] = cnt[node].copy()
                path[nxt] = [path[nxt][i] + tmp_path[i] + tmp_cnt[i] for i in range(20)]
                reroot(nxt, node)
                # 复原现场
                cnt[nxt] = p_nxt_cnt
                path[nxt] = p_node_path

        reroot(0, -1)
        return ans // 2
