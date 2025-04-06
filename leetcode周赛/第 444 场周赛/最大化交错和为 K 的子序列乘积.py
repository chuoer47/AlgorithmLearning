# coding=gb2312
from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # ����DPѹ���ռ�
        # ״̬���壺(�Ƿ�Ϊ��һ��ѡ��Ԫ�أ���ǰ����͵ķ��ţ�+1 �� -1����ǰ�����) => ��Ӧ�ĳ˻�����
        dp = defaultdict(set)
        # ��ʼ������ʼ״̬Ϊδѡ��Ԫ�أ�����Ϊ 0�������Ϊ 0���˻�Ϊ 1
        dp[(False, 0, 0)] = {1}
        # ��ʼ�����˻�Ϊ -1
        max_product = -1

        # ���������е�ÿ��Ԫ��
        for num in nums:
            # ���ڴ洢���º��״̬
            ndp = defaultdict(set)
            # ����ǰԪ�أ�����״̬
            for state, p_old in dp.items():
                # �����ǰ״̬
                has_old, sign_old, sum_old = state
                # ��ѡ��ǰԪ�أ�ֱ�Ӽ̳�֮ǰ��״̬�Ͷ�Ӧ�ĳ˻�����
                ndp[state] |= p_old

                # �Ѿ�ѡ�й�Ԫ��
                new_has = True
                # �л�����
                new_sign = (1 - sign_old) if has_old else 1
                # ����֮ǰ�ķ��ż����µĽ����
                new_sum = sum_old + (num if sign_old == 0 else -num)
                # �����µĳ˻�����,����˻����� limit��������Ϊ limit + 1
                new_p = {t * num if t * num <= limit else limit + 1 for t in p_old}

                # �µ�״̬
                new_state = (new_has, new_sign, new_sum)
                # ������״̬��Ӧ�ĳ˻�����
                ndp[new_state] |= new_p

            # ����״̬�ֵ�
            dp = ndp

        # Ѱ���������������˻�
        for state,current_p in dp.items():
            has_sel, _, _sum = state
            # ���Ѿ�ѡ�й�Ԫ���ҽ���͵��� k
            if has_sel and _sum == k:
                for t in current_p:
                    # ���˻������� limit����������˻�
                    if t <= limit:
                        max_product = max(t, max_product)
        return max_product
