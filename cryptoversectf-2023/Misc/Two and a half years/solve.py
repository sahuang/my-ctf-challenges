from pwn import *

def solve(n, h, a, p0, p1, p2):
    res_sum = 0
    # dp over nxh
    dp = [[0] * (h + 1) for _ in range(2)]
    dp[0][a] = 1
    for _ in range(1, n+1):
        for j in range(h+1):
            dp[1][j] = dp[0][j] * p1
            res_sum += dp[0][j] * p1 * j
            if j > 0:
                dp[1][j] += dp[0][j-1] * p2
                res_sum += dp[0][j-1] * p2 * (j - 0.5)
            else:
                dp[1][j] += dp[0][j] * p0
            if j < h:
                dp[1][j] += dp[0][j+1] * p0
                res_sum += dp[0][j+1] * p0 * (j + 0.5)
            else:
                dp[1][j] += dp[0][j] * p2
                res_sum += dp[0][j] * p2 * h
        dp[0] = [x for x in dp[1]]
    return res_sum

conn = remote("20.169.252.240", 4202)
for _ in range(20):
    conn.recvuntil(b":\n")
    n, h, a, p0, p1, p2 = map(int, conn.recvline().decode().split())
    res = solve(n, h, a, p0*0.01, p1*0.01, p2*0.01)
    print(res)
    conn.sendline(str(res).encode())
conn.interactive()