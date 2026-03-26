import math
from collections import defaultdict


def mo_query(arr, queries):
    """
    使用莫队算法解决区间不同元素数量查询问题

    莫队算法是一种高效处理离线区间查询的算法，通过合理排序查询区间，
    减少计算过程中的重复操作，从而优化时间复杂度。对于区间不同元素查询，
    算法时间复杂度约为 O((n√n) + q√n)，其中 n 是数组长度，q 是查询数量。

    参数:
        arr (list): 待查询的数组
        queries (list): 查询列表，每个查询是一个元组 (l, r)，
                       表示查询区间的左右端点（0-based 索引）

    返回:
        list: 每个查询对应的结果，即该区间内不同元素的数量

    示例:
        >>> arr = [1, 2, 1, 3, 2]
        >>> queries = [(0, 4), (1, 3), (2, 2)]
        >>> mo_query(arr, queries)
        [3, 3, 1]
    """
    n = len(arr)
    q = len(queries)
    if n == 0 or q == 0:
        return []

    # 块的大小，通常取 sqrt(n)
    block_size = int(math.sqrt(n)) + 1

    # 对查询进行排序，先按左端点所在块排序，再按右端点排序（偶奇排序优化）
    sorted_queries = [(queries[i][0], queries[i][1], i) for i in range(q)]
    sorted_queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))

    # 初始化变量
    current_l = 0
    current_r = -1
    freq = defaultdict(int)  # 记录元素出现频率
    distinct_count = 0  # 当前区间不同元素的数量
    result = [0] * q  # 存储查询结果

    # 处理每个查询
    for l, r, idx in sorted_queries:
        # 扩展或收缩左边界
        while current_l > l:
            current_l -= 1
            num = arr[current_l]
            if freq[num] == 0:
                distinct_count += 1
            freq[num] += 1
        while current_l < l:
            num = arr[current_l]
            freq[num] -= 1
            if freq[num] == 0:
                distinct_count -= 1
            current_l += 1

        # 扩展或收缩右边界
        while current_r < r:
            current_r += 1
            num = arr[current_r]
            if freq[num] == 0:
                distinct_count += 1
            freq[num] += 1
        while current_r > r:
            num = arr[current_r]
            freq[num] -= 1
            if freq[num] == 0:
                distinct_count -= 1
            current_r -= 1

        # 记录当前查询结果
        result[idx] = distinct_count

    return result
