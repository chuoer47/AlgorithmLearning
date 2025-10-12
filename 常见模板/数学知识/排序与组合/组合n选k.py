from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    """
    从1..n中选择k个元素的所有组合（不重复，不考虑顺序）

    参数:
        n: 元素范围（1到n）
        k: 选择的元素个数
    返回:
        所有可能的组合列表
    """
    result = []

    def backtrack(start: int, path: List[int]) -> None:
        # 终止条件：已选择k个元素
        if len(path) == k:
            result.append(path.copy())
            return

        # 从start开始遍历，避免重复组合（如[1,2]和[2,1]视为同一组合）
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)  # 下一次从i+1开始，确保顺序递增
            path.pop()  # 回溯

    backtrack(1, [])
    return result


# 示例用法
if __name__ == "__main__":
    n, k = 4, 2
    print(f"从1到{n}中选择{k}个元素的组合:")
    print(combine(n, k))
