from functools import lru_cache
from typing import List


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    记忆化DFS优化：从候选列表中选择元素（不可重复），使其和为目标值

    参数:
        candidates: 候选元素列表（可能含重复）
        target: 目标和
    返回:
        所有满足条件的不重复组合列表
    """
    # 预处理：排序（便于去重和剪枝）
    candidates.sort()
    n = len(candidates)

    @lru_cache(maxsize=None)
    def dfs(start: int, remaining: int) -> List[List[int]]:
        """
        记忆化DFS函数

        参数:
            start: 起始索引（避免重复组合，且确保元素不重复使用）
            remaining: 剩余需要达成的目标值
        返回:
            从start开始选择元素（不重复使用），和为remaining的所有组合列表
        """
        # 基本情况：找到有效组合
        if remaining == 0:
            return [[]]
        # 剪枝：剩余目标值为负，无需继续
        if remaining < 0:
            return []

        result = []
        prev = None  # 用于记录上一个元素，避免重复组合
        for i in range(start, n):
            num = candidates[i]
            # 去重：跳过与前一个元素相同的情况（因已排序）
            if num == prev:
                continue
            # 剪枝：当前元素大于剩余目标值，后续元素更大，直接跳出
            if num > remaining:
                break

            # 递归求解：选择当前元素后，下一轮从i+1开始（不可重复使用）
            sub_combinations = dfs(i + 1, remaining - num)

            # 将当前元素与子组合拼接
            for sub in sub_combinations:
                result.append([num] + sub)

            prev = num  # 更新上一个元素

        return result

    # 从索引0开始，目标值为target的所有组合
    return dfs(0, target)


# 示例用法
if __name__ == "__main__":
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8),  # 含重复元素的情况
        ([2, 5, 2, 1, 2], 5),
        ([1, 1], 2)
    ]

    for candidates, target in test_cases:
        print(f"候选元素: {candidates}, 目标和: {target}")
        combinations = combination_sum2(candidates, target)
        print(f"满足条件的组合: {combinations}")
        print(f"组合总数: {len(combinations)}\n")
