"""
https://www.acwing.com/problem/content/4969/
"""

s = input()
i = 0
res = 0
while i<len(s)-1:
    if s[i]==s[i+1] or s[i]=='?' or s[i+1]=='?':
        res+=1
        i+=1
    i+=1
print(res)