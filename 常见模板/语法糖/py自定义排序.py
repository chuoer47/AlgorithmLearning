'''
python自定义排序示例
该模块展示了如何通过重写类的比较方法来实现自定义排序逻辑
'''

class MnData:
    """
    存储包含名称和分数的数据类，支持自定义排序规则

    排序规则：
    1. 首先按照分数(score)升序排列（分数小的在前）
    2. 当分数相同时，按照名称(name)降序排列（字母顺序靠后的在前）
    """

    def __init__(self, name, score):
        """
        初始化MnData实例

        参数:
            name (str): 数据对应的名称
            score (int/float): 数据对应的分数值
        """
        self.name = name  # 存储名称信息
        self.score = score  # 存储分数信息

    def __lt__(self, other):
        """
        重写小于比较运算符，定义自定义排序逻辑
        该方法会被Python的sorted()等排序函数自动调用

        参数:
            other (MnData): 另一个MnData实例，用于比较

        返回:
            bool: 当self应该排在other前面时返回True，否则返回False
        """
        # 首先比较分数：当前实例分数小于另一个时，当前实例应排在前面
        if self.score < other.score:
            return True
        # 当分数相等时，比较名称：当前实例名称的字母顺序大于另一个时，当前实例应排在前面
        elif self.score == other.score:
            return self.name > other.name
        # 其他情况（当前分数大于另一个），当前实例应排在后面
        else:
            return False