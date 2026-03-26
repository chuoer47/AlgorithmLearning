# 如果是暴力求解
# 时间复杂度为 O(n*n*m*m)
# 异或有啥性质码？ 只记得 x^y^y = x
# 如果每次遍历mat2的时候，把mat1全体异或 pre^now可以吗
# 想不出来，暴力交一发，应该是写不出来这道题目了

mod = int(1e9 + 7)


def main():
    n, m = map(int, input().strip().split())
    mat1 = [list(map(int, input().strip().split())) for _ in range(n)]
    mat2 = [list(map(int, input().strip().split())) for _ in range(m)]
    ans = 0
    for i in range(0, n - m + 1):
        for j in range(0, n - m + 1):
            for k in range(0, m):
                for l in range(0, m):
                    ans = (ans + (mat1[i + k][j + l] ^ mat2[k][l])) % mod
    return ans % mod


if __name__ == '__main__':
    ans = main()
    print(ans)
