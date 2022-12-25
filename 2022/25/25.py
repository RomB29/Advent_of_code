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
    dividend = decimal_value + carry
    remainder = dividend % len(SNAFU_to_base_10)
    # Check if the remainder is outside the range of -2 to +2 if its the case, add a carry ± 1 
    if remainder < min(base_10_to_SNAFU):
        remainder +=len(SNAFU_to_base_10)
        carry = -1
    elif remainder > max(base_10_to_SNAFU):
        remainder -= len(SNAFU_to_base_10)
        carry = 1
    else:
        carry = 0
    decimal_value = dividend // len(SNAFU_to_base_10)
    reconvert.append(base_10_to_SNAFU[remainder])
    

result = "".join(reversed(reconvert))
# Reverse the result list and join the digits to obtain the SNAFU number
print(f"SNAFU number do you supply to Bob's console : {result}")

#    ___  ___  _  _  ___  ___  ___  ___    ___    _    ___  ___    ___  ___   _  _ __   __ ___  ___  _____   ___ __  __   _    __  __  ___  _     ___ 
#   / __|| __|| \| || __|| _ \|_ _|/ __|  | _ )  /_\  / __|| __|  / __|/ _ \ | \| |\ \ / /| __|| _ \|_   _| | __|\ \/ /  /_\  |  \/  || _ \| |   | __|
#  | (_ || _| | .` || _| |   / | || (__   | _ \ / _ \ \__ \| _|  | (__| (_) || .` | \ V / | _| |   /  | |   | _|  >  <  / _ \ | |\/| ||  _/| |__ | _| 
#   \___||___||_|\_||___||_|_\|___|\___|  |___//_/ \_\|___/|___|  \___|\___/ |_|\_|  \_/  |___||_|_\  |_|   |___|/_/\_\/_/ \_\|_|  |_||_|  |____||___|
                                                                                                                                                    

# Eg base 8:
# def my_base8(decimal_number):
#     base8_digits = []
#     while decimal_number > 0:
#         base8_digits.append(decimal_number % 8)
#         decimal_number //= 8
#     base8_digits.reverse()
#     base8_number = ''.join(str(d) for d in base8_digits)
#     return base8_number


