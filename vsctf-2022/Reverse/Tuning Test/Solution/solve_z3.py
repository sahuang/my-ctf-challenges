from z3 import *

def all_smt(s, initial_terms):
	def block_term(s, m, t):
		s.add(t != m.eval(t))
	def fix_term(s, m, t):
		s.add(t == m.eval(t))
	def all_smt_rec(terms):
		if sat == s.check():
		   m = s.model()
		   yield m
		   for i in range(len(terms)):
			   s.push()
			   block_term(s, m, terms[i])
			   for j in range(i):
				   fix_term(s, m, terms[j])
			   yield from all_smt_rec(terms[i:])
			   s.pop()
	yield from all_smt_rec(list(initial_terms))

flag = [BitVec('f_'+str(i), 8) for i in range(35)]
s = Solver()

for i in range(35):
	if i % 6 == 5:
		s.add(flag[i] == ord('-'))
	elif i % 12 in [6,7,8,9,10]:
		s.add(flag[i] == ord('X'))
	else:
		s.add(Or(And(flag[i] >= 48, flag[i] <= 57), And(flag[i] >= 65, flag[i] <= 90)))
s.add(flag[0]+flag[2]+flag[4]+flag[13]+flag[15]+flag[24]+flag[26]+flag[28] == 486)
s.add(flag[0]*flag[1]-flag[4]+flag[12]*flag[13]-flag[16]+flag[24]*flag[25]-flag[28] == 13713)
s.add(flag[3]*flag[14]*flag[27]-flag[2]*flag[15]*flag[25] == -6256)
s.add((flag[1]-flag[3])*flag[4] == 48)
s.add(((flag[13]<<3)-(flag[15]<<2))*flag[14] == 20604)
s.add(((flag[28]<<2)-(flag[0]<<2))*flag[27] == -5616)
s.add(flag[4]-flag[3]-flag[2]-flag[1]+flag[0]*flag[0] == 6744)
s.add(flag[16]-flag[15]-flag[14]-flag[13]+flag[12]*flag[12] == 2405)
s.add(flag[28]-flag[27]-flag[26]-flag[25]+flag[24]*flag[24] == 4107)
s.add(flag[14] < 58)
s.add((flag[14]+flag[24])*(flag[28]-flag[1]) == -1508)

for m in all_smt(s, flag):
	flag_bytes = bytes([m.eval(flag[i]).as_long() for i in range(len(flag))])
	print(flag_bytes)