def read_input():
    numbers = [int(n) for n in input().split(',')]
    boards = []
    try:
        while True:
            input()
            board = []
            for _ in range(5):
                board.append([int(n) for n in input().split()])
            boards.append(board)
    except Exception as e:
        print(e)
    return {'numbers': numbers, 'boards': boards}

def answer_01(numbers, boards):
    print(boards[1])
    verify_boards = []
    for _ in range(len(boards)):
        verify_board = []
        for i in range(len(boards[0])):
            verify_board.append([0 for _ in range(len(boards[0]))])
        verify_boards.append(verify_board)
    for number in numbers:
        for board_index in range(len(boards)):
            for i in range(len(boards[0])):
                for j in range(len(boards[0])):
                    if boards[board_index][i][j] == number:
                        verify_boards[board_index][i][j] = 1
            for i in range(len(boards[0])):
                if sum(verify_boards[board_index][i]) == len(boards[0]) or sum([verify_boards[board_index][j][i] for j in range(len(boards[0]))]) == len(boards[0]):
                    acc = 0
                    for i_verify in range(len(boards[0])):
                        for j_verify in range(len(boards[0])):
                            if verify_boards[board_index][i_verify][j_verify] == 0:
                                acc += boards[board_index][i_verify][j_verify]
                    return acc * number

def answer_02(numbers, boards):
    print(boards[1])
    verify_boards = []
    winners = []
    numbers_winners = []
    for _ in range(len(boards)):
        verify_board = []
        for i in range(len(boards[0])):
            verify_board.append([0 for _ in range(len(boards[0]))])
        verify_boards.append(verify_board)
    for number in numbers:
        for board_index in range(len(boards)):
            if board_index not in winners:
                for i in range(len(boards[0])):
                    for j in range(len(boards[0])):
                        if boards[board_index][i][j] == number:
                            verify_boards[board_index][i][j] = 1
                for i in range(len(boards[0])):
                    if sum(verify_boards[board_index][i]) == len(boards[0]) or sum(
                            [verify_boards[board_index][j][i] for j in range(len(boards[0]))]) == len(boards[0]):
                        winners.append(board_index)
                        numbers_winners.append(number)
    acc = 0
    print(winners[-1])
    for i_verify in range(len(boards[0])):
        for j_verify in range(len(boards[0])):
            if verify_boards[winners[-1]][i_verify][j_verify] == 0:
                acc += boards[winners[-1]][i_verify][j_verify]
    print(acc)
    return acc * numbers_winners[-1]




if __name__ == '__main__':
    input_ = read_input()
    print(answer_01(input_['numbers'], input_['boards']))
    print(answer_02(input_['numbers'], input_['boards']))

