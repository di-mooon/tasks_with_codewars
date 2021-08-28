def binary_to_string(binary):
    return ''.join([chr(int(binary[x:x + 8], base=2)) for x in range(0, len(binary), 8)])

binary_to_string('0100100001100101011011000110110001101111')
