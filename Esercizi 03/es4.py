from es1 import timer, farfallino3
# import es1
# import statistics as stat

@timer()
def hexstring2vec_v1(s: str) -> list[int]:
    # hex_pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    # result = [int(pair, 16) for pair in hex_pairs]
    result = [int(s[i:i+2], 16) for i in range(0, len(s), 2)]
    result.extend([0] * (8 - len(result)))
    return result

@timer()
def hexstring2vec_v2(s: str) -> list[int]:
    hex_list = []
    for i in range(0, 16, 2):
        hex_val = 0
        if i < len(s):
            hex_str = s[i:i+2]
            hex_val = int(hex_str, 16)
        hex_list.append(hex_val)
    return hex_list


from typing import Callable
def print_hexstring2vec(s: str, converter: Callable) -> None:
    print([f'0x{x:02X}' for x in converter(s)])
    #print([hex(x) for x in converter(s)])

print_hexstring2vec("12AB34CD56EF7890", hexstring2vec_v1)
print_hexstring2vec("12AB34CD56EF7890", hexstring2vec_v2)

print_hexstring2vec("12ab34cd56ef7890", hexstring2vec_v1)
print_hexstring2vec("12ab34cd56ef7890", hexstring2vec_v2)

print_hexstring2vec("35AF", hexstring2vec_v1)
print_hexstring2vec("35AF", hexstring2vec_v2)

print_hexstring2vec("0A0a0B0bcCdD", hexstring2vec_v1)
print_hexstring2vec("0A0a0B0bcCdD", hexstring2vec_v2)