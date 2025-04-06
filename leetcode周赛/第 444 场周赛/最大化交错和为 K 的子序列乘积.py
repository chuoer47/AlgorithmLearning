# coding=gb2312
from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # 滚动DP压缩空间
        # 状态定义：(是否为第一次选中元素；当前交错和的符号，+1 或 -1；当前交错和) => 对应的乘积集合
        dp = defaultdict(set)
        # 初始化：初始状态为未选中元素，符号为 0，交错和为 0，乘积为 1
        dp[(False, 0, 0)] = {1}
        # 初始化最大乘积为 -1
        max_product = -1

        # 遍历数组中的每个元素
        for num in nums:
            # 用于存储更新后的状态
            ndp = defaultdict(set)
            # 处理当前元素，更新状态
            for state, p_old in dp.items():
                # 解包当前状态
                has_old, sign_old, sum_old = state
                # 不选当前元素，直接继承之前的状态和对应的乘积集合
                ndp[state] |= p_old

                # 已经选中过元素
                new_has = True
                # 切换符号
                new_sign = (1 - sign_old) if has_old else 1
                # 根据之前的符号计算新的交错和
                new_sum = sum_old + (num if sign_old == 0 else -num)
                # 计算新的乘积集合,如果乘积超过 limit，则将其置为 limit + 1
                new_p = {t * num if t * num <= limit else limit + 1 for t in p_old}

                # 新的状态
                new_state = (new_has, new_sign, new_sum)
                # 更新新状态对应的乘积集合
                ndp[new_state] |= new_p

            # 更新状态字典
            dp = ndp

        # 寻找满足条件的最大乘积
        for state,current_p in dp.items():
            has_sel, _, _sum = state
            # 若已经选中过元素且交错和等于 k
            if has_sel and _sum == k:
                for t in current_p:
                    # 若乘积不超过 limit，则更新最大乘积
                    if t <= limit:
                        max_product = max(t, max_product)
        return max_product
