from Crypto.Util.number import *
from itertools import groupby

# Get signals
data = open('power_states.csv', 'r').read().splitlines()
states = [int(x.strip().split(",")[1]) for x in data[1:]]

# We would need to group 1's together similar to PicoChip 1
status = []
for k, g in groupby(states):
    if k != 0:
        status.append(sum(1 for _ in g))
    else:
        status.extend([0 for _ in g])
print(status)

status[0] -= 100 # Remove first 100 for prime generations

# By inspection, 210 is in the list and it separates p and q
idx = status.index(210)
status[idx] -= 110
# Count number of 0's between start and idx
count = 0
for i in range(1, idx):
    if status[i] == 0:
        count += 1
m_p = count
print(m_p)
# Count number of 0's between idx and end
count = 0
for i in range(idx, len(status)):
    if status[i] == 0:
        count += 1
m_q = count

# Get 100 odd primes
r = []
i = 3
while len(r) < 100:
    if isPrime(i):
        r.append(i)
    i += 2

# Get modulo equations for p
r_list_p = []
mod_list_p = []
i = 0
j = 0
while i < idx:
    if status[i] == 100:
        j += 1
        i += 2
    else:
        if r[status[i]] not in r_list_p:
            r_list_p.append(r[status[i]])
            mod_list_p.append(2*(m_p - j) % r[status[i]])
        j += 1
        i += 1 if status[i] == 0 else 2
print(r_list_p)
print(mod_list_p)

# Get modulo equations for q
r_list_q = []
mod_list_q = []
i = idx
j = 0
while i < len(status) - 1:
    if status[i] == 100:
        j += 1
        i += 2
    else:
        if r[status[i]] not in r_list_q:
            r_list_q.append(r[status[i]])
            mod_list_q.append(2*(m_q - j) % r[status[i]])
        j += 1
        i += 1 if status[i] == 0 else 2
print(r_list_q)
print(mod_list_q)

from sage.all import *
from math import prod

mod_p = CRT_list([1] + mod_list_p, [2] + r_list_p)
prod_p = prod(r_list_p) * 2
# print(f"p % {prod_p} == {mod_p}")

mod_q = CRT_list([1] + mod_list_q, [2] + r_list_q)
prod_q = prod(r_list_q) * 2
# print(f"q % {prod_q} == {mod_q}")

N = 130242563655857624894400945577596726349342500250110028576899185041437457270571385988775800707021082684571500938230335838572343683077030043170929464612371476956037213483889197399888953059037490955052374761877827022364642118001281744384383425614733953384975007872647643383223846078326219496054222658506664194809
e = 65537
ct = 105907761990378066226415220707780642346253492128869807523331608442629667283774856771483475721417798409391047173653877895381454531056957845466445503946203117753779878926970882151071816334395199925843076844258607834225532144320120475312185170491128333893223806872578843356036259570319998389877610989110147615590

a_p, s_p = mod_p, prod_p
a_q = pow(a_p, -1, s_p) * N % s_p
# print(f"q % {s_p} == {a_q}")

s = lcm(s_p, prod_q)
c_q = CRT_list([int(mod_q), int(a_q)], [int(prod_q), int(s_p)])
print(f"q % {s} == {c_q}")

b_q, s_q = mod_q, prod_q
b_p = pow(b_q, -1, s_q) * N % s_q
# print(f"p % {s_q} == {b_p}")

s2 = lcm(s_q, prod_p)
assert s2 == s
c_p = CRT_list([int(mod_p), int(b_p)], [int(prod_p), int(s_q)])
print(f"p % {s2} == {c_p}")