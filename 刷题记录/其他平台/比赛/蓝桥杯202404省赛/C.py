"""
在诗人的眼中，数字是生活的韵律，也是诗意的表达。
小蓝，当代顶级诗人与数学家，被赋予了 “数学诗人” 的美誉。他擅长将冰
冷的数字与抽象的诗意相融合，并用优雅的文字将数学之美展现于纸上。
某日，小蓝静坐书桌前，目光所及，展现着 n 个数字，它们依次为
a1, a2, . . . , an，熠熠生辉。小蓝悟到，如果一个数能够以若干个（至少两个）
连续的正整数相加表示，那么它就蕴含诗意。例如，数字 6 就蕴含诗意，因为
它可以表示为 1 + 2 + 3。而 8 则缺乏诗意，因为它无法用连续的正整数相加表
示。
小蓝希望他面前的所有数字都蕴含诗意，为此，他决定从这 n 个数字中删
除一部分。请问，小蓝需要删除多少个数字，才能使剩下的数字全部蕴含诗意？
"""
n = int(input())
q = list(map(int, input().split(" ")))
table = []
# 打表
table_len = 300
for i in range(1, table_len):
    for j in range(i + 2, table_len):
        t = 0
        for k in range(i, j):
            t += k
        table.append(t)
table = set(table)
res = 0
for i in q:
    if i not in table:
        res += 1
print(res)
