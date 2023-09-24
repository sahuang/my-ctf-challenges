from Crypto.Util.number import *
from mt19937predictor import MT19937Predictor
from pwn import *

def SmartAttack(P,Q,p):
    # copied from attack
    E = P.curve()
    Eqp = EllipticCurve(Qp(p, 2), [ ZZ(t) + randint(0,p)*p for t in E.a_invariants() ])
    P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
    for P_Qp in P_Qps:
        if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
            break
    Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
    for Q_Qp in Q_Qps:
        if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
            break
    p_times_P = p*P_Qp
    p_times_Q = p*Q_Qp
    x_P,y_P = p_times_P.xy()
    x_Q,y_Q = p_times_Q.xy()
    phi_P = -(x_P/y_P)
    phi_Q = -(x_Q/y_Q)
    k = phi_Q/phi_P
    return ZZ(k)

nums = []

conn = remote('172.86.96.174', int(4300))
# let's just do 80 connections since 80*8>624
for i in range(80):
    print(f"Connection {i+1}/80")
    conn.sendlineafter(b"Your choice: ", b"1")
    # p = ...
    rec = conn.recvline().strip().decode()
    p = int(rec.split(" = ")[1])
    # P = (x : y : 1)
    rec = conn.recvline().strip().decode()
    x0 = int(rec[rec.index("(")+1:rec.index(":")-1])
    y0 = int(rec[rec.index(":")+2:rec.index(": 1)")-1])
    # Q = (x : y : 1)
    rec = conn.recvline().strip().decode()
    x1 = int(rec[rec.index("(")+1:rec.index(":")-1])
    y1 = int(rec[rec.index(":")+2:rec.index(": 1)")-1])
    # Given p, x0, y0, x1, y1, find E(a, b) where P, Q are on E
    a = (y0**2 - y1**2 + x1**3 - x0**3) * inverse(x0-x1, p) % p
    b = (y0 ** 2 - x0 ** 3 - a * x0) % p
    E = EllipticCurve(GF(p), [a, b])
    P = E(x0, y0)
    Q = E(x1, y1)
    s = SmartAttack(P, Q, p)
    print(s)
    assert s < p
    s = [s & 0xffffffff, (s >> 32) & 0xffffffff, (s >> 64) & 0xffffffff, (s >> 96) & 0xffffffff, (s >> 128) & 0xffffffff, (s >> 160) & 0xffffffff, (s >> 192) & 0xffffffff, (s >> 224) & 0xffffffff]
    for i in range(8):
        nums.append(s[i])

predictor = MT19937Predictor()
for num in nums:
    predictor.setrandbits(num, 32)

conn.sendlineafter(b"Your choice: ", b"2")
conn.recvuntil(b"you: ")
res = int(conn.recvline().strip().decode(), 16)
print(res)
x, y = predictor.getrandbits(int(1337)), predictor.getrandbits(int(1337))
flag = (res - int(y)) // int(x)
print(long_to_bytes(int(flag)).decode())