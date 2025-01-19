"""
https://leetcode.cn/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(lst):
            lst = [ii for ii in lst if ii != "."]
            return len(set(lst)) == len(lst)

        # 对行列进行检查
        for i in range(9):
            if not check(board[i]):
                return False
            tem = []
            for j in range(9):
                tem.append(board[j][i])
            if not check(tem):
                return False

        # 对3*3矩阵检查
        for i in range(3):
            for j in range(3):
                tem = []
                for k in range(3):
                    tem.extend(board[k + 3 * j][3 * i:3 * i + 3])
                if not check(tem):
                    return False

        return True


if __name__ == '__main__':
    t = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "第 433 场周赛", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "第 433 场周赛", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    print(s.isValidSudoku(t))
