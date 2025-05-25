def group_knapsack(capacity, groups):
    """
    分组背包问题的动态规划解法

    参数:
    capacity (int): 背包的总容量
    groups (list): 物品分组列表，每个组是一个二维列表，
                  其中每个元素表示一个物品 [重量, 价值]

    返回:
    int: 背包能装下的最大价值
    """
    # 初始化动态规划数组，dp[j] 表示容量为 j 时的最大价值
    dp = [0] * (capacity + 1)

    # 遍历每个物品组
    for group in groups:
        # 对于每个容量，需要逆序更新以避免重复选择同一组的物品
        for j in range(capacity, -1, -1):
            # 遍历当前组中的每个物品
            for item in group:
                weight, value = item[0], item[1]
                # 如果物品重量小于等于当前容量，考虑是否选择该物品
                if weight <= j:
                    dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


# 示例使用
if __name__ == "__main__":
    # 背包总容量
    capacity = 10
    # 物品分组：每个组内只能选择一个物品
    groups = [
        [[2, 3], [3, 4]],  # 第一组物品：[重量2,价值3], [重量3,价值4]
        [[4, 5], [5, 6]],  # 第二组物品：[重量4,价值5], [重量5,价值6]
        [[6, 7]]  # 第三组物品：[重量6,价值7]
    ]

    max_value = group_knapsack(capacity, groups)
    print(f"背包能装下的最大价值是: {max_value}")
