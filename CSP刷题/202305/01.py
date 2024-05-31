"""
该题核心思想为利用字典进行哈希，快速查找，降低时间复杂度
"""

n = int(input())
arr_str = []
for i in range(0, n):
    tem = ""
    for j in range(0,8):
        tem = tem + str(input())
    arr_str.append(tem)
res = []
str_dict = dict()
for i in range(0,n):
    if arr_str[i] in str_dict:
        value = str_dict[arr_str[i]]
        str_dict[arr_str[i]] = value + 1
        res.append(value+1)
    else:
        value = 1
        str_dict[arr_str[i]] = value
        res.append(1)
for i in range(0,n):
    print(res[i])
