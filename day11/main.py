def read_input():
    energy_levels = []
    try:
        while True:
            energy_levels.append([int(c) for c in list(input())])
    except Exception as e:
        print(e)
    return energy_levels


def increase_energy_levels(energy_levels, to_increase, already_flash):
    for i in range(len(to_increase)):
        for j in range(len(to_increase[i])):
            if energy_levels[i][j] <= 9 and not already_flash[i][j]:
                energy_levels[i][j] += to_increase[i][j]
            to_increase[i][j] = 0
    return energy_levels, to_increase


def flash_energy_levels(energy_levels, to_increase, already_flash):
    num_flashes = 0
    for i in range(len(to_increase)):
        for j in range(len(to_increase[i])):
            if energy_levels[i][j] > 9 and not already_flash[i][j]:
                num_flashes += 1
                energy_levels[i][j] = 0
                already_flash[i][j] = True
                directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
                for direction in directions:
                    i_new = i + direction[0]
                    j_new = j + direction[1]

                    if 0 <= i_new < len(to_increase) \
                            and 0 <= j_new < len(to_increase[i_new]) \
                            and not already_flash[i_new][j_new]:
                        to_increase[i_new][j_new] += 1

    return energy_levels, to_increase, already_flash, num_flashes


def check_energy_to_flash(energy_levels):
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            if energy_levels[i][j] > 9:
                return True
    return False


def all_flashed(energy_levels):
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            if energy_levels[i][j] != 0:
                return False
    return True


def answer_01(energy_levels):
    num_flashes = 0
    for _ in range(100):
        to_increase = []
        already_flash = []
        for i in range(len(energy_levels)):
            to_increase.append([1 for j in range(len(energy_levels[i]))])
            already_flash.append([False for j in range(len(energy_levels[i]))])
        energy_levels, to_increase = increase_energy_levels(energy_levels, to_increase, already_flash)
        while True:
            energy_levels, to_increase, already_flash, num_flash = flash_energy_levels(energy_levels, to_increase, already_flash)
            num_flashes += num_flash
            energy_levels, to_increase = increase_energy_levels(energy_levels, to_increase, already_flash)
            has_energy_to_flash = check_energy_to_flash(energy_levels)
            if not has_energy_to_flash:
                break
        print("Round {}".format(_))

    return num_flashes


def answer_02(energy_levels):
    num_flashes = 0
    turn = 1
    while not all_flashed(energy_levels):
        to_increase = []
        already_flash = []
        for i in range(len(energy_levels)):
            to_increase.append([1 for j in range(len(energy_levels[i]))])
            already_flash.append([False for j in range(len(energy_levels[i]))])
        energy_levels, to_increase = increase_energy_levels(energy_levels, to_increase, already_flash)
        while True:
            energy_levels, to_increase, already_flash, num_flash = flash_energy_levels(energy_levels, to_increase,
                                                                                       already_flash)
            num_flashes += num_flash
            energy_levels, to_increase = increase_energy_levels(energy_levels, to_increase, already_flash)
            has_energy_to_flash = check_energy_to_flash(energy_levels)
            if not has_energy_to_flash:
                break
        print("Round {}".format(turn))

        for energy_level in energy_levels:
            print(energy_level)
        if all_flashed(energy_levels):

            break

        turn+=1

    return num_flashes


if __name__ == '__main__':
    energy_levels = read_input()
    print(answer_01(energy_levels))
    print(answer_02(energy_levels))