"""
https://www.acwing.com/problem/content/1275/

ST表模板可以秒杀，不过ST表老忘记怎么打
emmmmm，基本功不扎实
"""


class SparseTable:
    """
    稀疏表

    核心思想为倍增法
    st[i][j] => 区间[i,i+2^j-1]的属性
    st[i][j] = func{st[i][j-1],st[i-2^(j-1)][j-1]}
    注: func 具有区间不变性！

    查询操作:
    query [l,r] => func{ st[l][s] , st[r-2^s+1][s] }  s = log2(r-l+1) 取下整
    """

    def __init__(self, data, func=max):
        self.st = st = [list(data)]
        self.func = func
        n = len(data)
        i = 1
        # 这里建表使用了倍增的方法，而算是间接采用动态规划的思想，可以节约不少建表时间
        # 同时把i,j的坐标对换了
        # 可以简单的理解：i控制当前跳越的间隔，j表示根据当前的跳越间隔最多存在几个数字存在st的当前行
        # [1,2,3,4,5,6,7,8]
        # 一开始i=1，间隔为2,得到7个元素存在第二行的st表
        # 然后i=2,间隔为4，得到5个元素存在第三行st表
        # i=3，间隔为8，存在1个元素在第四行st表
        # 至此，算法结束
        while 2 * i <= n:
            pre = st[-1]
            st.append([func(pre[j], pre[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, left, right):
        s = (right - left + 1).bit_length() - 1
        return self.func(self.st[s][left], self.st[s][right - (1 << s) + 1])


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().strip().split(" ")))
    st = SparseTable(data=lst)
    query = int(input())
    for _ in range(query):
        begin, end = list(map(int, input().strip().split(" ")))
        print(st.query(begin-1, end-1))
