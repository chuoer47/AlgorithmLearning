class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in dic.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if t!=dic[i]:
                    return False
        return not stack
