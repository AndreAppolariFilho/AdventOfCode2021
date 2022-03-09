import numpy as np
from math import prod

def read_input():
    matrix_python = []
    try:
        while True:
            matrix_python.append([int(i) for i in input()])
    except Exception as e:
        print(e)

    matrix = np.array(matrix_python)
    return matrix


def get_neighbours(matrix, row_idx, column_idx):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = []
    for (x, y) in directions:
        offset_x = column_idx + x
        offset_y = row_idx + y

        if 0 <= offset_y < matrix.shape[0] and 0 <= offset_x < matrix.shape[1]:
            neighbours.append(matrix[offset_y][offset_x])
    return neighbours


def get_neighbours_positions(matrix, row_idx, column_idx):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = []
    for (x, y) in directions:
        offset_x = column_idx + x
        offset_y = row_idx + y
        if 0 <= offset_y < matrix.shape[0] and 0 <= offset_x < matrix.shape[1]:
            neighbours.append((offset_y, offset_x))
    return neighbours


def is_smaller_point(matrix, row_idx, column_idx):
    for neighbour in get_neighbours(matrix, row_idx, column_idx):
        if neighbour <= matrix[row_idx][column_idx]:
            return False
    return True


def get_basin_points(matrix, row_idx, column_idx, basin_points=set()):
    if (row_idx, column_idx) in basin_points:
        return basin_points
    if matrix[row_idx][column_idx] == 9:
        return basin_points
    basin_points.add((row_idx, column_idx))
    for (pos_y, pos_x) in get_neighbours_positions(matrix, row_idx, column_idx):
        basin_points = get_basin_points(matrix, pos_y, pos_x, basin_points)
    return basin_points


def answer_01(matrix):
    response_answer = 0
    for row_column, row_value in np.ndenumerate(matrix):
        row_idx = row_column[0]
        column_idx = row_column[1]
        if is_smaller_point(matrix, row_idx, column_idx):

            response_answer += (1 + row_value)
    return response_answer


def answer_02(matrix):
    basin_sizes = []
    for row_column, row_value in np.ndenumerate(matrix):
        row_idx = row_column[0]
        column_idx = row_column[1]
        if is_smaller_point(matrix, row_idx, column_idx):
            basin_sizes.append(len(get_basin_points(matrix, row_idx, column_idx, set())))
    return prod(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    matrix = read_input()
    print(answer_01((matrix)))
    print(answer_02((matrix)))
