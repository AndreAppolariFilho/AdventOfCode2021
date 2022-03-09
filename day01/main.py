def read_input():
    list_of_numbers = []
    try:
        while True:
            list_of_numbers.append(int(input()))
    except Exception as e:
        print(e)
    return list_of_numbers

def count_increasing(list_of_numbers):
    counter = 0
    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index] > list_of_numbers[index - 1]:
            counter+=1
    return counter

def count_increasing_part_2(list_of_numbers):
    counter = 0
    for index in range(len(list_of_numbers)-3):
        sum_1 = sum([list_of_numbers[index], list_of_numbers[index + 1], list_of_numbers[index + 2]])
        sum_2 = sum([list_of_numbers[index+1], list_of_numbers[index + 2], list_of_numbers[index + 3]])
        if sum_1 < sum_2:
            counter+=1

    return counter

if __name__ == '__main__':
    list_of_numbers = read_input()
    print(count_increasing(list_of_numbers))
    print(count_increasing_part_2(list_of_numbers))
