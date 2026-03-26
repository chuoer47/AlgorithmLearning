from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    生成无重复元素列表的所有全排列

    参数:
        nums: 不含重复元素的列表
    返回:
        所有可能的全排列列表
    """
    result = []
    n = len(nums)
    used = [False] * n  # 标记元素是否已使用

    def backtrack(path: List[int]) -> None:
        # 终止条件：路径长度等于元素总数
        if len(path) == n:
            result.append(path.copy())
            return

        for i in range(n):
            if not used[i]:
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
    nums = [1, 2, 3]
    print(f"输入列表: {nums}")
    print(f"所有全排列: {permute(nums)}")
    print(f"排列总数: {len(permute(nums))}")
