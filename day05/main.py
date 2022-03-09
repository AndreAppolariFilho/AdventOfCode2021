def read_input():
    positions = []
    try:
        while True:
            line = input()
            position = []
            for command in line.split(' -> '):
                position.append([int(i) for i in command.split(',')])
            positions.append(position)
    except Exception as e:
        print(e)
    return positions

def answer_01(commands):
    length = 0
    for command in commands:
        for position in command:
            for number in position:
                length = max(number, length)
    matrix = [[0 for i in range(length+1)] for j in range(length+1)]

    for command in commands:

        if command[0][0] == command[1][0]:
            end = max(command[0][1], command[1][1])
            start = min(command[0][1], command[1][1])
            for i in range(start, end+1):
                matrix[i][command[0][0]] += 1

        elif command[0][1] == command[1][1]:
            end = max(command[0][0], command[1][0])
            start = min(command[0][0], command[1][0])
            for i in range(start, end+1):

                matrix[command[0][1]][i] += 1
    n_intersections = 0
    for row in matrix:
        for number in row:

            if number >= 2:
                n_intersections+=1
    return n_intersections

def answer_02(commands):
    length = 0
    for command in commands:
        for position in command:
            for number in position:
                length = max(number, length)
    matrix = [[0 for i in range(length+1)] for j in range(length+1)]

    for command in commands:

        if command[0][0] == command[1][0]:
            end = max(command[0][1], command[1][1])
            start = min(command[0][1], command[1][1])
            for i in range(start, end+1):
                matrix[i][command[0][0]] += 1

        elif command[0][1] == command[1][1]:
            end = max(command[0][0], command[1][0])
            start = min(command[0][0], command[1][0])
            for i in range(start, end+1):
                matrix[command[0][1]][i] += 1
        else:
            start_point = [command[0][0], command[0][1]]
            matrix[start_point[1]][start_point[0]] += 1
            while True:
                if command[0][0] > command[1][0]:
                    if start_point[0] <= command[1][0]:
                        break
                    start_point[0] -= 1
                else:
                    if start_point[0] >= command[1][0]:
                        break
                    start_point[0] += 1
                if command[0][1] > command[1][1]:
                    if start_point[1] <= command[1][1]:
                        break
                    start_point[1] -= 1
                else:
                    if start_point[1] >= command[1][1]:
                        break
                    start_point[1] += 1

                matrix[start_point[1]][start_point[0]] += 1

    n_intersections = 0
    for row in matrix:
        for number in row:
            if number >= 2:
                n_intersections+=1
    return n_intersections

if __name__ == '__main__':
    commands = read_input()
    print(answer_01(commands))
    print(answer_02(commands))