def add_bits(bits_a, bits_b):
    r = 0
    bits_c = []
    for i in range(len(bits_a) - 1, -1, -1):
        s = bits_a[i] + bits_b[i] + r
        bits_c = [s % 2] + bits_c
        if s > 1:
            r = 1
        else:
            r = 0
    bits_c = [r] + bits_c
    return bits_c


b1 = [1, 0, 1, 1]
b2 = [1, 1, 0, 1]
print(add_bits(b1, b2))  # should be 11000
