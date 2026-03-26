import random


class RandomizedSet:

    def __init__(self):
        self.dic = dict()

    def insert(self, val: int) -> bool:
        if val in self.dic.keys():
            return False
        self.dic[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic.keys():
            return False
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        if not self.dic:
            return None
        random_value = random.choice(list(self.dic.values()))
        return random_value


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val=5)
param_1 = obj.insert(val=3)
param_1 = obj.insert(val=4)
param_2 = obj.remove(val=0)
param_3 = obj.getRandom()
print(param_3)
