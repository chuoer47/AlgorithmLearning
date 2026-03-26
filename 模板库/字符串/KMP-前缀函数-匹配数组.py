"""
KMP算法（Knuth-Morris-Pratt算法）实现

算法功能：在主串中高效查找模式串的出现位置
核心优势：通过前缀函数预处理模式串，避免无效字符比较，实现线性时间复杂度
时间复杂度：O(n + m)，其中n为主串长度，m为模式串长度
空间复杂度：O(m)，用于存储前缀函数数组
"""


def prefix_function(pattern: str) -> list:
    """计算模式串的前缀函数数组（最长前缀后缀数组）

    前缀函数定义：对于模式串pattern的第i个位置，pi[i]是满足以下条件的最大整数k：
    1. k < i（前缀长度小于当前位置）
    2. pattern[0..k-1] == pattern[i-k..i-1]（前缀与后缀相等）
    这是KMP算法的核心预处理步骤，用于指导匹配过程中的回溯

    参数:
        pattern: 待处理的模式串（需要查找的子串）

    返回:
        list: 前缀函数数组，长度与模式串相同，pi[i]表示对应位置的最长前缀后缀长度
    """
    m = len(pattern)
    pi = [0] * m  # 初始化前缀数组，长度为模式串长度

    # 从第二个字符开始计算（第一个字符的前缀函数必为0）
    for i in range(1, m):
        # j初始化为前一个位置的前缀函数值（最大可能的匹配长度）
        j = pi[i - 1]

        # 若当前字符不匹配，通过前缀函数回溯j，寻找更短的可能匹配
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        # 若当前字符匹配，延长前缀长度
        if pattern[i] == pattern[j]:
            j += 1

        # 记录当前位置的最长前缀后缀长度
        pi[i] = j

    return pi


def kmp_search(main_str: str, pattern: str) -> list:
    """使用KMP算法在主串中查找模式串的所有出现位置

    算法思路：
    1. 对模式串进行预处理，计算前缀函数数组
    2. 将模式串、特殊分隔符（防止跨界匹配）和主串拼接
    3. 计算拼接字符串的前缀函数，当前缀函数值等于模式串长度时，说明找到匹配

    参数:
        main_str: 主串（被查找的字符串）
        pattern: 模式串（需要查找的子串）

    返回:
        list: 所有匹配位置的起始索引列表（主串中），若未找到则返回空列表
    """
    n = len(main_str)
    m = len(pattern)

    # 边界情况处理：模式串为空或长于主串时直接返回空
    if m == 0 or m > n:
        return []

    # 拼接模式串、分隔符和主串（分隔符需是不在两串中出现的字符）
    combined = pattern + '#' + main_str
    # 计算拼接字符串的前缀函数
    prefix_lst = prefix_function(combined)

    # 收集所有匹配位置
    match_positions = []
    # 遍历前缀函数结果（从模式串长度+1开始，对应主串部分）
    for i in range(m + 1, len(prefix_lst)):
        # 当前缀函数值等于模式串长度时，说明找到匹配
        if prefix_lst[i] == m:
            # 计算主串中匹配的起始位置
            start_index = i - 2 * m
            match_positions.append(start_index)

    return match_positions


# 示例用法
if __name__ == "__main__":
    # 示例1：基本匹配
    main_str1 = "ababaababaca"
    pattern1 = "abab"
    print(f"主串: {main_str1}")
    print(f"模式串: {pattern1}")
    print(f"匹配位置: {kmp_search(main_str1, pattern1)}")  # 输出: [0, 2, 6]

    # 示例2：重复字符匹配
    main_str2 = "aaaaa"
    pattern2 = "aa"
    print(f"\n主串: {main_str2}")
    print(f"模式串: {pattern2}")
    print(f"匹配位置: {kmp_search(main_str2, pattern2)}")  # 输出: [0, 1, 2, 3]

    # 示例3：无匹配情况
    main_str3 = "abcdefg"
    pattern3 = "xyz"
    print(f"\n主串: {main_str3}")
    print(f"模式串: {pattern3}")
    print(f"匹配位置: {kmp_search(main_str3, pattern3)}")  # 输出: []
