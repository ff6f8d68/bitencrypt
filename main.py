# main.py

import base64

def text_to_ascii_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bitflip(bits):
    return ''.join('1' if b == '0' else '0' for b in bits)

def generate_key(ascii_bits):
    # ALG1: Just sum the bits (number of 1's)
    ones_count = ascii_bits.count('1')
    # To avoid trivial keys, force minimum flipping distance
    key = max(2, ones_count % 7 + 2)  # Key will be between 2 and 8
    return key

def algorithmic_bitflip(bits, key):
    result = []
    one_counter = 0
    for bit in bits:
        result.append(bit)
        if bit == '1':
            one_counter += 1
        if one_counter == key:
            if len(result) > 0:
                result[-1] = '1' if result[-1] == '0' else '0'
            one_counter = 0
    return ''.join(result)

def bits_to_base64(bits):
    chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    byte_array = bytearray(int(chunk, 2) for chunk in chunks)
    base64_string = base64.b64encode(byte_array).decode('utf-8')
    return base64_string

def hash_password(text):
    ascii_bits = text_to_ascii_bits(text)
    key = generate_key(ascii_bits)
    flipped_bits = bitflip(ascii_bits)
    final_bits = algorithmic_bitflip(flipped_bits, key)
    base64_hash = bits_to_base64(final_bits)
    return base64_hash, key
