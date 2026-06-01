def myAtoi(s):
    # Skip leading whitespace
    s = s.strip()
    if not s:
        return 0

    i = 0
    sign = 1
    result = 0

    # Optional leading + or - (only one sign is read)
    if s[i] == '-' or s[i] == '+':
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Build integer from consecutive digits; stop at first non-digit
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        # Clamp to 32-bit signed int range before overflow
        if result > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
        result = result * 10 + digit
        i += 1

    return sign * result

print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("3.14159"))
print(myAtoi("+-12"))
print(myAtoi("0032"))
print(myAtoi("   +0 123"))
print(myAtoi("2147483648"))
print(myAtoi("-2147483649"))