from subprocess import Popen, PIPE
import os

# read string
with open("in", "r") as f:
	input = f.read()

with open("template.cpp", "r") as f:
	code = f.read()

# len(input) = 51236
# 39*1337 - 51236 = 907 to pad
input += "0" * 907
assert len(input) == 1337 * 39
input = [input[i:i+39] for i in range(0, len(input), 39)]

# generate elf for each string
for i in range(1337):
	p = Popen(["./gen"], stdout=PIPE, stdin=PIPE)
	tmp = input[i] + '\n'
	p.stdin.write(tmp.encode())
	p.stdin.flush()

	result = p.stdout.readline().strip()
	# feed the result to template code
	replaced_code = code.replace("REDACTED", result.decode())
	with open("tmp.cpp", "w") as f:
		f.write(replaced_code)
	os.system("g++ -s -std=c++11 tmp.cpp -o file_" + str(i))