from functools import lru_cache
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    记忆化DFS优化：从候选列表中选择元素（可重复），使其和为目标值

    参数:
        candidates: 候选元素列表（可能含重复）
        target: 目标和
    返回:
        所有满足条件的不重复组合列表
    """
    # 预处理：去重+排序，避免重复组合并便于剪枝
    candidates = sorted(list(set(candidates)))
    n = len(candidates)

    @lru_cache(maxsize=None)
    def dfs(start: int, remaining: int) -> List[List[int]]:
        """
        记忆化DFS函数

        参数:
            start: 起始索引（避免重复组合，确保元素按顺序选择）
            remaining: 剩余需要达成的目标值
        返回:
            从start开始，和为remaining的所有组合列表
        """
        #  base case: 剩余目标值为0，返回包含空列表的列表（表示一种有效组合的结束）
        if remaining == 0:
            return [[]]

        result = []
        for i in range(start, n):
            num = candidates[i]
            # 剪枝：当前元素大于剩余目标值，无需继续（因已排序）
            if num > remaining:
                break

            # 递归求解：选择当前元素后，剩余目标值减少num，且下一轮可重复选择当前元素（故start仍为i）
            sub_combinations = dfs(i, remaining - num)

            # 将当前元素与子组合拼接，形成完整组合
            for sub in sub_combinations:
                result.append([num] + sub)

        return result

    # 从索引0开始，目标值为target的所有组合
    return dfs(0, target)


# 示例用法
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([1], 1)
    ]

    for candidates, target in test_cases:
        print(f"候选元素: {candidates}, 目标和: {target}")
        print(f"满足条件的组合: {combination_sum(candidates, target)}")
        print(f"组合总数: {len(combination_sum(candidates, target))}\n")
