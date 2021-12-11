def parse_input(lines):
    return [line.split(' | ') for line in lines]

def part_one(lines):
    count = 0
    desired_lens = set([2, 3, 4, 7])
    for _, output in lines:
        count += sum([1 for x in output.split(' ') if len(x) in desired_lens])

    return count

def part_two(lines):
    r = []
    for display_str, output_str in lines:
        display, output = display_str.split(' '), output_str.split(' ')

        decoder = compute_decoder(display)

        num = []
        for code in output:
            code = ''.join(sorted(code))
            num.append(str(decoder[code]))

        r.append(int(''.join(num)))

    return sum(r)

"""
2: [1]
3: [7]
4: [4]
5: [2, 3, 5]
6: [0, 6, 9]
7: [8]
"""
def compute_decoder(display):
    unique_len_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }

    code_to_number_map = {}
    number_to_code_map = {}
    candidates = {}

    # do obvious nums first
    for code in display:
        if len(code) in unique_len_map:
            code_to_number_map[code] = unique_len_map[len(code)]
            number_to_code_map[unique_len_map[len(code)]] = code

    two_three_five = [code for code in display if len(code) == 5]
    zero_six_nine = [code for code in display if len(code) == 6]


    # find 0
    c = {}
    for code in two_three_five:
        for letter in code:
            if letter in c:
                c[letter] += 1
                continue
            c[letter] = 1

    u = [l for l, count in c.items() if count != 3]

    for code in zero_six_nine:
        s = set(code)
        if all(l in s for l in u):
            code_to_number_map[code] = 0
            number_to_code_map[0] = code
            break

    # figure out six and nine
    six_nine = [code for code in zero_six_nine if code != number_to_code_map[0]]
    one_code = number_to_code_map[1]
    for code in six_nine:
        s = set(code)

        if all(x in s for x in one_code):
            code_to_number_map[code] = 9
            number_to_code_map[9] = code
        else:
            code_to_number_map[code] = 6
            number_to_code_map[6] = code

    # figure out 5
    six_code = set(number_to_code_map[6])
    for code in two_three_five:
        if all(x in six_code for x in code):
            code_to_number_map[code] = 5
            number_to_code_map[5] = code
            break

    # figure out two and three
    two_three = [code for code in two_three_five if code != number_to_code_map[5]]
    for code in two_three:
        if all(x in code for x in one_code):
            code_to_number_map[code] = 3
            number_to_code_map[3] = code
        else:
            code_to_number_map[code] = 2
            number_to_code_map[2] = code

    return {''.join(sorted(c)): n for c, n in code_to_number_map.items()}
 
if __name__ == '__main__':
    with open('inp.txt') as f:
        lines = parse_input([x.strip('\n') for x in f.readlines()])

    print(part_one(lines))
    print(part_two(lines))
