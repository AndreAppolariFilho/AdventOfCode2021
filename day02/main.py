def read_input():
    list_of_comands = []
    try:
        while True:
            command = input()

            list_of_comands.append(command)
    except Exception as e:
        print(e)
    return list_of_comands

def answer_01(list_of_commands):
    width = 0
    depth = 0
    for line in list_of_commands:
        command, amount = line.split(" ")
        if command == 'forward':
            width += int(amount)
        if command == 'down':
            depth += int(amount)
        if command == 'up':
            depth -= int(amount)
    return width * depth

def answer_02(list_of_commands):
    width = 0
    depth = 0
    aim = 0
    for line in list_of_commands:
        command, amount = line.split(" ")
        if command == 'forward':
            width += int(amount)
            depth += aim * int(amount)
        if command == 'down':
            aim += int(amount)
        if command == 'up':
            aim -= int(amount)
    return width * depth
if __name__ == '__main__':
    list_of_commands = read_input()
    print(answer_01(list_of_commands))
    print(answer_02(list_of_commands))