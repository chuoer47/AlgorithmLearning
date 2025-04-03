class MnData:
    # 适用最小堆的数据
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or (self.score == other.score and self.name > other.name)