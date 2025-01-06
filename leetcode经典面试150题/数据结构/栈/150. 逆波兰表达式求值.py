"""
https://leetcode.cn/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    plus = lambda x, y: x + y
    minus = lambda x, y: x - y
    multi = lambda x, y: x * y

    def divide(x, y):
        if x / y >= 0:
            return x // y
        else:
            if x // y == x / y:
                return x // y
            return x // y + 1

    dic = {"+": plus, "-": minus, "*": multi, "/": divide}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in self.dic.keys():
                stack.append(int(i))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(self.dic[i](x, y))
        return stack.pop()


tokens = ["10", "6", "9", "3", "+", "-第 147 场双周赛", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(tokens))
