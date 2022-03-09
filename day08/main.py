def read_input():
    output_ = []
    input_ = []
    try:
        while True:
            i, o = input().split(' | ')
            input_.append(i)
            output_.append(o)
    except Exception as e:
        pass
    return [input_, output_]


def answer_1(output_):
    return sum([
        1
        for row in output_
        for digit in row.split(' ')
        if len(digit) in [2, 4, 3, 7]
    ])

def all_digits_in(digit, comparision):
    return all(item in digit for item in comparision)

def all_digits_that_contains_len(digits, length):
    return [digit for digit in digits if len(digit) == length]

def answer_2(input_, output_):
    counter = 0
    for i in range(len(input_)):
        digits = input_[i].split(' ')

        one = all_digits_that_contains_len(digits, 2)[0]
        four = all_digits_that_contains_len(digits, 4)[0]
        seven = all_digits_that_contains_len(digits, 3)[0]
        eight = all_digits_that_contains_len(digits, 7)[0]
        three = 0
        for digit in all_digits_that_contains_len(digits, 5):
            if all_digits_in(digit, one):
                three = digit
                break

        nine = 0
        for digit in all_digits_that_contains_len(digits, 6):
            if all_digits_in(digit, four):
                nine = digit
                break
        zero = 0
        for digit in all_digits_that_contains_len(digits, 6):
            if digit == nine:
                continue
            if all_digits_in(digit, one):
                zero = digit
            else:
                six = digit

        two = 0
        five = 0

        for digit in all_digits_that_contains_len(digits, 5):
            if digit == three:
                continue

            if all_digits_in(six, digit):
                five = digit
            else:
                two = digit

        mapping_segments = {
            zero:'0',
            one:'1',
            two:'2',
            three:'3',
            four:'4',
            five:'5',
            six:'6',
            seven:'7',
            eight:'8',
            nine:'9'
        }

        o = tuple((output_[i].split(' ')))

        answer = ""
        for digit in o:
            for key in mapping_segments:

                if len(set(key) & set(digit)) == len(digit) and len(key) == len(digit):

                    answer += mapping_segments[key]
                    break
        counter += int(answer)

    return counter


if __name__ == '__main__':
    input_, output_ = read_input()
    print(output_)
    print(answer_1(output_))
    print(answer_2(input_, output_))