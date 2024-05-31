def dot(a: list, b: list, n1, d, n2) -> list:
    res = []
    for i in range(0, n1):
        tem = []
        for j in range(0, n2):
            t = 0
            for k in range(0, d):
                t = t + a[i][k] * b[k][j]
            tem.append(t)
        res.append(tem)
    return res


def ddot(w: list, a: list, n , d) -> list:
    res = []
    for i in range(0, n):
        tem = []
        wi = w[i]
        for j in range(0, d):
            tem.append(a[i][j] * wi)
        res.append(tem)
    return res


if __name__ == '__main__':
    n, d = map(int, input().split(" "))
    tem = []
    for i in range(0, 3 * n + 1):
        tem.append(list(map(int, input().split(" "))))
    # 前置工作
    Q = []
    K = []
    V = []
    W = tem[-1]
    for i in range(0, n):
        Q.append(tem[i])
        K.append(tem[i + n])
        V.append(tem[i + 2 * n])
    # print(Q, K, V, W)

    KT = []
    for i in range(0, d):
        tem = []
        for j in range(0, n):
            tem.append(K[j][i])
        KT.append(tem)

    KTV = dot(KT, V, d, n, d)
    # print(KTV)
    QKTV = dot(Q, KTV, n, d, d)
    # print(QKTV)
    WQKTV = ddot(W, QKTV, n, d)

    arr_res = []
    for i in range(0, n):
        res = ""
        for j in range(0, d):
            res = res + " " + str(WQKTV[i][j])
        arr_res.append(res)
    for i in range(0, n):
        print(arr_res[i][1::1])
