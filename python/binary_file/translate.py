def binary_to_string(binary_data: bytes) -> str:
    return ''.join(f'{byte:08b}' for byte in binary_data)

def string_to_binary(bit_string: str) -> bytes:
    padded = bit_string + '0' * ((8 - len(bit_string) % 8) % 8)
    byte_list = [int(padded[i:i+8], 2) for i in range(0, len(padded), 8)]
    return bytes(byte_list)


# b'\x01\x02\xff'
def loop_bytes(bytes):
    for b in bytes:
        yield b


def test_binary_to_string_basic():
    assert binary_to_string(b'\x01\x02\xff') == '000000010000001011111111'

def test_binary_to_string_empty():
    assert binary_to_string(b'') == ''

def test_string_to_binary_basic():
    bit_str = '000000010000001011111111'
    assert string_to_binary(bit_str) == b'\x01\x02\xff'

def test_string_to_binary_padding():
    # 12 bits, should pad 4 zeros to make 16 bits (2 bytes)
    bit_str = '101010101010'
    expected = bytes([0b10101010, 0b10100000])
    assert string_to_binary(bit_str) == expected

def test_string_to_binary_empty():
    assert string_to_binary('') == b''

def test_round_trip():
    original = b'\x10\x20\x30\x40'
    bit_str = binary_to_string(original)
    restored = string_to_binary(bit_str)
    assert restored == original
