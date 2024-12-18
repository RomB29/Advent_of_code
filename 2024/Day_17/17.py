import sys
import re
import heapq
from collections import defaultdict, Counter, deque
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '17.in'
ans = 0
D = open(infile).read().strip()

regs, program = D.split('\n\n')
A,B,C = ints(regs)
program = program.split(':')[1].strip().split(',')
program = [int(x) for x in program]
#print(A,B,C,program)


def run(A):
    def getCombo(x):
        if x in [0,1,2,3]:
            return x
        if x==4:
            return A
        if x==5:
            return B
        if x==6:
            return C
        return -1
    ip = 0
    out = []

    while ip < len(program):
        cmd = program[ip]
        if cmd == 0:
            A = A // 2**getCombo(program[ip + 1])
            ip += 2
        elif cmd == 1:
            B = B ^ program[ip + 1]
            ip += 2
        elif cmd == 2:
            B = getCombo(program[ip + 1]) % 8
            ip += 2
        elif cmd == 3:
            if A != 0:
                ip = program[ip + 1]
            else:
                ip += 2
        elif cmd == 4:
            B = B ^ C
            ip += 2
        elif cmd == 5:
            out.append(getCombo(program[ip + 1]) % 8)
            ip += 2
        elif cmd == 6:
            B = A // 2**getCombo(program[ip + 1])
            ip += 2
        elif cmd == 7:
            C = A // 2**getCombo(program[ip + 1])
            ip += 2


    print(','.join([str(x) for x in out]))
    return out

out = []
while out != program:
    if len(out) < len(program):
        out = run(A)
        A += 100000
    else:
        out = run(A)
        A -= 1

print(A - 1)
print(','.join([str(x) for x in out]))