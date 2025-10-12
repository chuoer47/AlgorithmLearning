from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    生成多重集的所有独特排列

    参数:
        nums: 包含重复元素的列表（多重集）

    返回:
        所有不重复的排列列表
    """
    # 排序是去重的关键前提
    nums.sort()
    n = len(nums)
    result = []
    used = [False] * n  # 标记元素是否已被使用

    def backtrack(path: List[int]) -> None:
        """回溯函数生成排列"""
        # 终止条件：路径长度等于元素总数
        if len(path) == n:
            result.append(path.copy())
            return

        for i in range(n):
            # 跳过已使用的元素
            if used[i]:
                continue

            # 跳过重复元素：当前元素与前一个元素相同，且前一个元素未被使用
            # 确保相同元素按顺序使用，避免重复排列
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # 选择当前元素
            used[i] = True
            path.append(nums[i])

            # 递归探索
            backtrack(path)

            # 回溯：撤销选择
            path.pop()
            used[i] = False

    backtrack([])
    return result


# 示例用法
if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [2, 2, 1, 1],
        [1, 2, 3]  # 无重复元素的情况也适用
    ]

    for i, nums in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"输入多重集: {nums}")
        permutations = permute_unique(nums)
        print(f"所有独特排列 ({len(permutations)} 个):")
        for p in permutations:
            print(p)
        print()
