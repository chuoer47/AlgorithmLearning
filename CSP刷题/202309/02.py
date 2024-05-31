from math import cos, sin


class Operation:
    def __init__(self, k, det):
        self.k = k
        self.det = det


n, m = map(int, input().split(" "))
arr_op = []
arr_res = []
for i in range(0, n):
    arr_op.append(
        list(map(float, input().split(" ")))
    )
for i in range(0, m):
    arr_res.append(
        list(map(int, input().split(" ")))
    )
arr_op_sum = [Operation(1, 0)]
for i in range(0, n):
    option, var = arr_op[i]
    before = arr_op_sum[i]
    k, det = before.k, before.det
    if option == 1:
        k = before.k * var
    else:
        det = before.det + var
    arr_op_sum.append(Operation(k, det))

res = []
for i in range(0, m):
    begin, end, x, y, = arr_res[i]
    begin_op, end_op = arr_op_sum[begin - 1], arr_op_sum[end]
    x, y = (x * cos(end_op.det) - y * sin(end_op.det)) * end_op.k, (
                x * sin(end_op.det) + y * cos(end_op.det)) * end_op.k
    x, y = (x * cos(begin_op.det) + y * sin(begin_op.det)) / begin_op.k,  ((-1)*
                x * sin(begin_op.det) + y * cos(begin_op.det)) / begin_op.k
    res.append([x, y])
for i in range(0, m):
    print("%.3f %.3f" % (res[i][0], res[i][1]))
