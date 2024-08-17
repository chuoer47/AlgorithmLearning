"""
https://www.acwing.com/problem/content/5157/
"""

from collections import Counter

n = int(input())
s = input()
MOD = 10 ** 9 + 7
cnt = Counter(s)
max_num = 0
diff = 1
for c in ['A', 'C', 'G', 'T']:
    if cnt[c] > max_num:
        max_num = cnt[c]
        diff = 1
    elif cnt[c] == max_num:
        diff += 1
print(pow(diff, n, MOD))
