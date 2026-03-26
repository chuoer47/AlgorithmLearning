from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from typing import List


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.sl = deque()
        self.record_destination = defaultdict(deque)
        self.vis = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        comb = (timestamp, source, destination)
        if comb in self.vis:
            return False
        self.vis.add(comb)
        if len(self.sl) == self.memoryLimit:
            self.forwardPacket()
        self.sl.append(comb)
        self.record_destination[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.sl:
            return []
        timestamp, source, destination = self.sl.popleft()
        self.record_destination[destination].popleft()
        self.vis.remove((timestamp, source, destination))
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        nums = self.record_destination[destination]
        left = bisect_left(nums, startTime)  # nums[left] >= startTime
        right = bisect_right(nums, endTime) - 1  # nums[right] <= endTime
        return right - left + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# ©leetcode
