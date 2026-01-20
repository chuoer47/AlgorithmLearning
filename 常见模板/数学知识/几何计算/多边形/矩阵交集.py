class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        # 交集左下角x = 两个矩形左下角x的较大值
        inter_x1 = max(x11, x21)
        # 交集左下角y = 两个矩形左下角y的较大值
        inter_y1 = max(y11, y21)
        # 交集右上角x = 两个矩形右上角x的较小值
        inter_x2 = min(x12, x22)
        # 交集右上角y = 两个矩形右上角y的较小值
        inter_y2 = min(y12, y22)

        # 判断是否存在有效交集（交集区域必须是正的，即左下角<右上角）
        return inter_x1 < inter_x2 and inter_y1 < inter_y2
