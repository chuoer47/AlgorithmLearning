from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class TaskManager:
    # 最大堆

    def __init__(self, tasks: List[List[int]]):
        sl = SortedList()
        task2user = defaultdict(tuple)
        for uid, tid, pri in tasks:
            sl.add((pri, tid, uid))
            task2user[tid] = (pri, uid)
        self.sl = sl
        self.task2user = task2user

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sl.add((priority, taskId, userId))
        self.task2user[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        sl = self.sl
        task2user = self.task2user
        pri, uid = task2user[taskId]
        sl.remove((pri, taskId, uid))
        self.add(uid, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        sl = self.sl
        task2user = self.task2user
        pri, uid = task2user[taskId]
        sl.remove((pri, taskId, uid))
        task2user[taskId] = tuple

    def execTop(self) -> int:
        if not self.sl:
            return -1
        pri, tid, uid = self.sl.pop(-1)
        self.task2user[tid] = tuple()
        return uid

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()©leetcode
