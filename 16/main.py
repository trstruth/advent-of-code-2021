def parse_input(lines):
    return lines[0]

def hex_to_bin(h):
    mapping = {
            "0" : "0000",
            "1" : "0001",
            "2" : "0010",
            "3" : "0011",
            "4" : "0100",
            "5" : "0101",
            "6" : "0110",
            "7" : "0111",
            "8" : "1000",
            "9" : "1001",
            "A" : "1010",
            "B" : "1011",
            "C" : "1100",
            "D" : "1101",
            "E" : "1110",
            "F" : "1111",
            }

    return "".join(mapping[c] for c in h)

def custom_mul(arg):
    prod = 1
    for x in arg:
        prod *= x

    return prod


class Solution:
    def __init__(self):
        self.version_sum = 0
        self.fn_mapping = {
                0: sum,
                1: custom_mul,
                2: min,
                3: max,
                5: lambda x: 1 if x[0] > x[1] else 0,
                6: lambda x: 1 if x[0] < x[1] else 0,
                7: lambda x: 1 if x[0] == x[1] else 0,
                }


    def decode_one_packet(self, b):
        # print(f'\n\n\nDECODING: {b}')
        version = int(b[:3], 2)
        type_ID = int(b[3:6], 2)
        rest = b[6:]

        self.version_sum += version

        if type_ID == 4:
            # print(f'is literal')
            idx = 6
            s = ''
            while True:
                stop, num = b[idx], b[idx+1 : idx+5]
                s += (num)

                if stop == '0':
                    idx += 5
                    break

                idx += 5

            return int(s, 2), b[idx:]


        length_type_id = b[6]
        operator = self.fn_mapping[type_ID]

        if length_type_id == '0':
            # print(f'is operator with bit length mode')
            sub_packet_bit_length = int(b[7:22], 2)
            c = b[22:22+sub_packet_bit_length]

            packets = []
            while len(c) > 0:
                x, c = self.decode_one_packet(c)
                packets.append(x)

            # print(f'running {operator} on {packets}')
            return operator(packets), b[22+sub_packet_bit_length:]

        else:
            # print(f'is operator with num packets mode')
            packets = []
            num_packets = int(b[7:18], 2)
            b = b[18:]
            for _ in range(num_packets):
                x, b = self.decode_one_packet(b)
                packets.append(x)

            # print(f'running {operator} on {packets}')
            return operator(packets), b

def part_one(inp):
    s = Solution()
    s.decode_one_packet(hex_to_bin(inp))
    return s.version_sum

def part_two(inp):
    s = Solution()
    res, _ = s.decode_one_packet(hex_to_bin(inp))
    return res

if __name__ == '__main__':
    with open('inp.txt') as f:
        inp = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(inp))
    print(part_two(inp))
