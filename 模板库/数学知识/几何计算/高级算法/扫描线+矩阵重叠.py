from typing import List


class Solution:
    """
    解决850. 矩形面积 II问题的类

    问题描述：计算多个轴对齐矩形所覆盖的总面积，重叠部分只计算一次。
    解法采用扫描线算法，通过处理水平和垂直方向的边界来高效计算总面积。
    """

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        计算多个矩形覆盖的总面积

        参数:
            rectangles: 矩形列表，每个矩形由[x1, y1, x2, y2]表示，其中
                        (x1, y1)是左下角坐标，(x2, y2)是右上角坐标

        返回:
            int: 矩形覆盖的总面积对10^9 + 7取模的结果
        """
        # 收集所有矩形的上下边界（y坐标），用于划分y轴区间
        hbound = set()
        for rect in rectangles:
            # 添加下边界y1
            hbound.add(rect[1])
            # 添加上边界y2
            hbound.add(rect[3])

        # 将y坐标排序，形成有序的y轴分割点
        hbound = sorted(hbound)
        m = len(hbound)
        # seg数组用于记录每个y区间被矩形覆盖的次数，长度为m-1（m个点形成m-1个区间）
        seg = [0] * (m - 1)

        # 构建扫描线事件列表：记录所有矩形的左右边界
        # 每个元素为(x坐标, 矩形索引, 标记)，标记1表示左边界（进入矩形），-1表示右边界（离开矩形）
        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界事件
            sweep.append((rect[0], i, 1))
            # 右边界事件
            sweep.append((rect[2], i, -1))
        # 按x坐标排序，确保按从左到右的顺序处理边界
        sweep.sort()

        ans = 0
        i = 0  # 扫描线事件索引
        while i < len(sweep):
            j = i
            # 找到所有x坐标相同的事件（同一垂直线上的所有边界）
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1

            # 如果已经处理到最后一个事件，无需继续计算
            if j + 1 == len(sweep):
                break

            # 一次性处理当前x坐标下的所有边界事件，更新seg数组
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                # 获取当前矩形的y范围
                left_y, right_y = rectangles[idx][1], rectangles[idx][3]
                # 遍历所有y区间，更新被覆盖次数
                for x in range(m - 1):
                    # 若当前y区间完全在矩形的y范围内，则更新覆盖计数
                    if left_y <= hbound[x] and hbound[x + 1] <= right_y:
                        seg[x] += diff

            # 计算当前x区间内，被覆盖的y方向总长度
            cover = 0
            for k in range(m - 1):
                # 若该y区间被至少一个矩形覆盖，则累加其高度
                if seg[k] > 0:
                    cover += (hbound[k + 1] - hbound[k])

            # 累加面积：当前x区间宽度 * 被覆盖的y总长度
            ans += cover * (sweep[j + 1][0] - sweep[j][0])

            # 移动到下一组x坐标事件
            i = j + 1

        # 返回结果对10^9 + 7取模
        return ans % (10 ** 9 + 7)