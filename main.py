from heapq import *


class MnData:
    # 适用最小堆的数据
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.name > other.name)


class MxData:
    # 适用最大堆的数据
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score > other.score or (self.score == other.score and self.name < other.name)


class SORTracker:

    def __init__(self):
        self.upper = []  # 最小堆
        self.lower = []  # 最大堆
        self.k = 0

    def add(self, name: str, score: int) -> None:
        data = heappushpop(self.upper, MnData(name=name, score=score))
        heappush(self.lower, MxData(name=data.name, score=data.score))

    def get(self) -> str:
        data = heappop(self.lower)
        heappush(self.upper, MnData(name=data.name, score=data.score))
        ans = self.upper[0]
        return ans.name


if __name__ == '__main__':
    s = SORTracker()
    s.add("bradford", 2)
    s.add("branford", 3)
    print(s.get())
    s.add("alps", 2)
    print(s.get())
