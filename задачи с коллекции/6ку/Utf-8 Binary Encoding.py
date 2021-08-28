def to_utf8_binary(string):
    bits = bin(int.from_bytes(string.encode('ascii',), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def from_utf8_binary(bitstring):
    n = int(bitstring, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('ascii')


