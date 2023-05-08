import time
from random import randint
from math import fabs

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

flag = "cvctf{m4yb3_MASTER.MA_n3xt_y34r!}"

print("Solve 20 test cases, each within 5 seconds.")
for ca in range(1, 21):
    print(f"Test case {ca}:")
    n = randint(1, 100000)
    h = randint(0, 100)
    a = randint(0, h)
    # p0 + p1 + p2 == 100
    p0 = randint(0, 100)
    p1 = randint(0, 100 - p0)
    p2 = 100 - p0 - p1
    res = solve(n, h, a, p0/100.0, p1/100.0, p2/100.0)
    print(f"{n} {h} {a} {p0} {p1} {p2}")

    t = time.time()
    ans = float(input())
    if fabs(ans - res) > 1e-6:
        print("Wrong answer!")
        exit(1)
    if time.time() - t > 5:
        print("Time limit exceeded!")
        exit(1)

print("Correct! Here is your flag: " + flag)
