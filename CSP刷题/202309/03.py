MOD = 10 ** 9 + 7


class Node:
    def __init__(self, char, value, left=None, right=None):
        self.char = char  # 该字符
        self.value = value  # 该点的值
        self.left = left
        self.right = right


def trans_tree(express, value):  # 根据逆波兰式构造二叉树
    stack_l = express
    stack_r = []
    for i in range(len(stack_l)):
        c = stack_l[i]
        if c == 'x':
            stack_r.append(Node(c, value))
        elif c == '*':
            op1 = stack_r.pop()
            op2 = stack_r.pop()
            stack_r.append(Node(c, value=(op1.value * op2.value) % MOD, left=op1, right=op2))
        elif c == '+':
            op1 = stack_r.pop()
            op2 = stack_r.pop()
            stack_r.append(Node(c, value=(op1.value + op2.value) % MOD, left=op1, right=op2))
        elif c == '-':
            op1 = stack_r.pop()
            op2 = stack_r.pop()
            stack_r.append(Node(c, value=(op2.value - op1.value) % MOD, left=op2, right=op1))
        else:
            stack_r.append(Node(c, int(c)))
    return stack_r.pop()


def cal(node: Node):  # 根据构造的二叉树计算偏导值
    c = node.char
    if c == "x":
        return 1
    elif c == "*":
        return (cal(node.left) * node.right.value + cal(node.right) * node.left.value) % MOD
    elif c == "+":
        return (cal(node.left) + cal(node.right)) % MOD
    elif c == "-":
        return (cal(node.left) - cal(node.right)) % MOD
    else:
        return 0


def cal_tree(express, value):
    return cal(trans_tree(express, value))


# res = trans_tree("x x * x * 0 + -100000 -100000 * x * -", -1)
# r = cal(res)
# print(r)


n, m = map(int, input().split(" "))
express = list(input().split(" "))  # 变为数组
arr = [[int(i) for i in input().split(" ")] for _ in range(0, m)]
res = []
for i in range(0, m):
    k = arr[i][0]
    express_new = express.copy()
    for j in range(0, len(express_new)):
        c = express_new[j][0]
        if c == "x":
            num = int(express_new[j][1::1])
            if num == k:
                express_new[j] = "x"
            else:
                express_new[j] = str(arr[i][num])
    res.append(cal_tree(express_new, arr[i][k]) % MOD)
for i in range(len(res)):
    print(res[i])
