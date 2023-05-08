from sage.all import *
from pwn import *

conn = remote("67.205.179.135", 7272)
conn.recvline()

for _ in range(10):
    weights = eval(conn.recvline().strip().decode())
    values = eval(conn.recvline().strip().decode())
    capacity = int(conn.recvline().strip().decode().split(": ")[1])
    n = len(weights)

    dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1],
                            dp[i - 1][j - weights[i - 1]] - values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    result = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            result.append(i - 1)
            j -= weights[i - 1]

    # sanity check weights
    assert sum([weights[i] for i in result]) <= capacity

    conn.sendlineafter(b"Items: ", " ".join([str(i) for i in result[::-1]]).encode())
    print(conn.recvline().strip().decode())

print(conn.recvline().strip().decode())

for _ in range(10):
    M = eval(conn.recvline().strip().decode())
    ct = int(conn.recvline().strip().decode().split(": ")[1])
    n = len(M)
    L = matrix.zero(n + 1)
    for row, x in enumerate(M):
        L[row, row] = 2
        L[row, -1] = x
    L[-1, :] = 1
    L[-1, -1] = ct

    res = L.LLL()
    res = [1 if i == -1 else 0 for i in res[0][:-1]]
    res = int("".join([str(i) for i in res]), 2)
    print(f"r: {res}")

    conn.sendlineafter(b"Secret: ", str(res).encode())
    print(conn.recvline().strip().decode())

print(conn.recvline().strip().decode())