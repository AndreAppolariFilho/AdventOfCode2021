def read_input():
    list_of_binaries = []
    try:
        while True:
            command = input()
            list_of_binaries.append(command)
    except Exception as e:
        print(e)
    return list_of_binaries

def answer_1(list_of_binaries):
    most_common_sum = 0
    least_common_sum = 0
    for j in range(len(list_of_binaries[0])):
        quantity_1 = 0
        quantity_0 = 0
        for i in range(len(list_of_binaries)):
            if list_of_binaries[i][j] == '1':
                quantity_1 += 1
            if list_of_binaries[i][j] == '0':
                quantity_0 += 1
        if quantity_1 > quantity_0:
            most_common_sum+=2**(len(list_of_binaries[0]) - j - 1) * 1
        else:
            least_common_sum+=2**(len(list_of_binaries[0]) - j - 1) * 1
    return most_common_sum * least_common_sum

def answer_2(list_of_binaries):
    most_common_word = ''
    least_common_word = ''
    matched = list_of_binaries.copy()
    matched_lest_common = list_of_binaries.copy()
    for j in range(len(list_of_binaries[0])):
        if len(matched) > 1:
            quantity_1 = 0
            quantity_0 = 0
            for i in range(len(matched)):
                if matched[i][j] == '1':
                    quantity_1 += 1
                if matched[i][j] == '0':
                    quantity_0 += 1
            if quantity_0 > quantity_1:
                most_common_word+= '0'
            else:
                most_common_word+='1'
            matched = [binary for binary in matched if binary.startswith(most_common_word)]

        if len(matched_lest_common) > 1:
            quantity_1 = 0
            quantity_0 = 0

            for i in range(len(matched_lest_common)):
                if matched_lest_common[i][j] == '1':
                    quantity_1 += 1
                if matched_lest_common[i][j] == '0':
                    quantity_0 += 1
            if quantity_0 > quantity_1:
                least_common_word+='1'
            else:
                least_common_word += '0'

            matched_lest_common = [binary for binary in matched_lest_common if binary.startswith(least_common_word)]


    return int(matched[0],2) * int(matched_lest_common[0], 2)
if __name__ == '__main__':
    list_of_binaries = read_input()
    print(answer_1(list_of_binaries))
    print(answer_2(list_of_binaries))