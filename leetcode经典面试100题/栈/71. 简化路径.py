"""
https://leetcode.cn/problems/simplify-path/submissions/547646805/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = list(path.split("/"))
        lst = [i for i in lst if i and i != "."]
        stack = ["#"]
        for i in lst:
            if i == "..":
                if stack[-1] != "#":
                    stack.pop()
            else:
                stack.append(i)
        res = "/"
        for i in stack[1:]:
            res += str(i) + "/"
        return res[:-1] if res[:-1] else "/"


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/../"))
