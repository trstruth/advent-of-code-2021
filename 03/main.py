def parse_input(lines):
    return lines

def part_one(lines):
    zero_bit_counts = [0 for _ in range(len(lines[0]))]

    for binary_number_str in lines:
        for idx, bit in enumerate(binary_number_str):
            if bit == '0':
                zero_bit_counts[idx] += 1

    gamma_rate = ''.join('0' if count > len(lines) / 2 else '1' for count in zero_bit_counts)
    epsilon_rate = ''.join('0' if c == '1' else '1' for c in gamma_rate)

    gamma_rate = int('0b' + gamma_rate, 2)
    epsilon_rate = int('0b' + epsilon_rate, 2)

    return gamma_rate * epsilon_rate

def part_two(lines):

    oxygen_generator_rating = int('0b' + filter_by_criteria(lines, compute_one_bit_criteria), 2)
    co2_scrubber_rating = int('0b' + filter_by_criteria(lines, compute_zero_bit_criteria), 2)

    return oxygen_generator_rating * co2_scrubber_rating

def compute_one_bit_criteria(lines):
    one_bit_counts = [0 for _ in range(len(lines[0]))]

    for binary_number_str in lines:
        for idx, bit in enumerate(binary_number_str):
            if bit == '1':
                one_bit_counts[idx] += 1

    return ''.join('1' if count >= len(lines) / 2 else '0' for count in one_bit_counts)

def compute_zero_bit_criteria(lines):
    zero_bit_counts = [0 for _ in range(len(lines[0]))]

    for binary_number_str in lines:
        for idx, bit in enumerate(binary_number_str):
            if bit == '0':
                zero_bit_counts[idx] += 1

    return ''.join('0' if count <= len(lines) / 2 else '1' for count in zero_bit_counts)

def filter_by_criteria(lines, criteria):
    idx = 0

    while len(lines) > 1:
        criteria_str = criteria(lines)
        lines = [x for x in lines if x[idx] == criteria_str[idx]]
        idx += 1

    return lines[0]



if __name__ == '__main__':
    with open('inp1.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
