# Example values
a = 5   # 0101 in binary
b = 3   # 0011 in binary

# Bitwise AND
result_and = a & b  # Result: 0001
print(result_and)

# Bitwise OR
result_or = a | b   # Result: 0111
print(result_or)

# Bitwise XOR
result_xor = a ^ b  # Result: 0110
print(result_xor)

# Bitwise NOT
result_not_a = ~a   # Result: -6 (due to two's complement representation)
print(result_not_a)

# Left Shift
left_shifted = a << 2  # Result: 010100 (20 in decimal)
print(left_shifted)

# Right Shift
right_shifted = a >> 1  # Result: 0010 (2 in decimal)
print(right_shifted)
