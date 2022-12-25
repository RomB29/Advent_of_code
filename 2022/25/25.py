filename = "25.in"

with open(filename, 'r') as f:
    datas = f.read().strip().split("\n")

SNAFU_to_base_10 = {
    "0" : 0, 
    "1": 1,  
    "2": 2, 
    "-": -1, 
    "=": -2
    }

base_10_to_SNAFU = {
        0: "0",
        1: "1",
        2: "2",
        -1: "-",
        -2: "=",
    }

decimal_conversion = []
for SNAFU_number in datas:
    width = len(SNAFU_number)
    digits = list(reversed(SNAFU_number))
    decimal_conversion.append(sum(SNAFU_to_base_10[d] * 5**i for i, d in enumerate(digits)))
decimal_value = sum(decimal_conversion)

reconvert = []
carry = 0

# Divide the decimal number by the base until the quotient is less than the base
while abs(decimal_value + carry) > 0:
    # Add the carry to the dividend
    dividend = decimal_value + carry
    # Append the remainder to the result list
    remainder = dividend % len(SNAFU_to_base_10)
    # Check if the remainder is outside the range of -2 to +2
    if remainder < min(base_10_to_SNAFU):
        remainder +=len(SNAFU_to_base_10)
        carry = -1
    elif remainder > max(base_10_to_SNAFU):
        remainder -= len(SNAFU_to_base_10)
        carry = 1
    else:
        carry = 0
    # Append the modified remainder to the result list
    reconvert.append(base_10_to_SNAFU[remainder])
    # Update the dividend for the next division
    decimal_value = dividend // len(SNAFU_to_base_10)


# Append the final quotient to the result list
result = "".join(reversed(reconvert))


    # Reverse the result list and join the digits to obtain the SNAFU number
print(f"SNAFU number do you supply to Bob's console : {result}")
