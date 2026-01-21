import heapq
from collections import defaultdict


class AuctionSystem:

    def __init__(self):
        # 权威数据源：{物品ID: {用户ID: 最新出价金额}}
        self.mapper = defaultdict(lambda: defaultdict(int))
        # 懒删除最大堆：{物品ID: 堆}
        # 堆元素改为 (-出价金额, -用户ID)：
        # 1. -出价金额：实现出价从高到低（最小堆模拟最大堆）
        # 2. -用户ID：出价相同时，-userId更小的（原userId更大）优先在堆顶
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        """添加出价：堆中存储(-bidAmount, -userId)以满足规则"""
        self.mapper[itemId][userId] = bidAmount
        # 核心修改：入堆元素增加对userId取负
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        """更新出价：同addBid逻辑"""
        self.mapper[itemId][userId] = newAmount
        heapq.heappush(self.heaps[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        """移除出价：仅修改权威数据源"""
        if userId in self.mapper[itemId]:
            del self.mapper[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        """获取最高出价者：适配新的堆元素结构，且出价相同时返回更大的userId"""
        # 1. 检查权威数据源是否有有效出价
        item_bids = self.mapper[itemId]
        if not item_bids:
            return -1

        heap = self.heaps[itemId]

        # 2. 懒删除无效数据
        while heap:
            # 取出堆顶：注意堆中是(-出价, -用户ID)
            neg_amount, neg_user_id = heap[0]
            current_amount = -neg_amount
            current_user_id = -neg_user_id

            # 核对：用户存在且出价匹配权威数据
            if current_user_id in item_bids and item_bids[current_user_id] == current_amount:
                return current_user_id
            else:
                # 数据过期，弹出堆顶
                heapq.heappop(heap)

        # 理论上不会走到这（因item_bids非空）
        return -1