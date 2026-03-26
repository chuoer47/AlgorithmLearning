from random import random

MAX_LEVEL = 32
P_FACTOR = 0.25


def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random() < P_FACTOR:
        lv += 1
    return lv


class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level


class Skiplist:

    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        if cur is None or cur.val != num:
            return False
        for i in range(0, self.level):
            if update[i].forward[i] != cur:
                break
            update[i].forward[i] = cur.forward[i]
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)