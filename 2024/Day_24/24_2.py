file = open("24_rework.in")

known = {}

for line in file:
    if line.isspace():
        break
    x, y = line.split(": ")
    known[x] = int(y)

formulas = {}

for line in file:
    x, op, y, z = line.replace(" ->", " ").split()
    formulas[z] = (op, x, y)

operators = {
    "OR" : lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y
}

def calc(wire):
    if wire in known:
        return known[wire]
    op, x, y = formulas[wire]
    known[wire] = operators[op](calc(x), calc(y))
    return known[wire]

z = []
i = 0

while True:
    key = "z" + str(i).rjust(2, "0")
    if key not in formulas:
        break
    z.append(calc(key))
    i += 1

print(int("".join(map(str, z[::-1])), 2))

# Credit: HyperNeutrino
# Helper functions
def make_wire(prefix, num):
    """Create a wire name like x00, y03, z01."""
    return f"{prefix}{str(num).zfill(2)}"

def verify_z(wire, num):
    """Verify if the final output wire z[num] produces the correct value."""
    print("vz", wire, num)
    if wire not in formulas:
        return False
    op,x,y = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

def verify_intermediate_xor(wire, num):
    """Check if a wire correctly computes an intermediate XOR value."""
    print("vx", wire, num)
    if wire not in formulas:
        return False
    op,x,y = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    """Check if a wire correctly computes a carry bit."""
    print("vc", wire, num)
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if num == 1:
        return op == "AND" and sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return (verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1)) or \
           (verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1))

def verify_direct_carry(wire, num):
    """Check if a wire computes a direct carry."""
    print("vd", wire, num)
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    """Check if a wire correctly propagates a carry bit."""
    print("vr", wire, num)
    if wire not in formulas:
        return False
    op,x,y = formulas[wire]
    if op != "AND":
        return False
    return (verify_intermediate_xor(x, num) and verify_carry_bit(y, num)) or \
           (verify_intermediate_xor(y, num) and verify_carry_bit(x, num))

def verify(num):
    """Verify if the output for the nth bit is correct."""
    return verify_z(make_wire("z", num), num)

def progress():
    """Find the maximum number of bits correctly computed by the system."""
    i = 0
    while verify(i):
        i += 1
    return i

def debug_print(wire, depth=0):
    if wire[0] in "xy":
        return "  " * depth + wire
    op, x, y = formulas[wire]
    return "  " * depth + op + " (" + wire + ")\n" + debug_print(x, depth + 1) + "\n" + debug_print(y, depth + 1)
# Find the swaps
# i = 0
# while True:
#     if not verify(i):
#         break
#     i += 1

print(debug_print("z01"))
verify(0)
print("Failed on", make_wire("z", i))


# z08 <-> ffj
# dwp <-> kfm
# z22 <-> gjh
# z31 <-> jdr

test = ["z08", "ffj", "dwp", "kfm", "z22", "gjh", "z31", "jdr"]