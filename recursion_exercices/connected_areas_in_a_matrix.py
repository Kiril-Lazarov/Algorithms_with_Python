m = int(input())
n = int(input())

matrix = [list(input()) for x in range(m)]

directions = ['right', 'down', 'left', 'up']
areas = [0]
final_info = {}


def moves(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


def check_cell(new_row, new_col):
    if 0 <= new_row < m and 0 <= new_col < n:
        return True
    return False


def connect_areas(row, col):
    if matrix[row][col] != '-':
        return

    areas[0] += 1
    matrix[row][col] = 'V'

    for direction in directions:
        new_row, new_col = moves(row, col, direction)
        if check_cell(new_row, new_col):
            connect_areas(new_row, new_col)


for row in range(m):
    for col in range(n):
        if matrix[row][col] == '-':
            connect_areas(row, col)
            if areas[0] > 0:
                final_info[(row, col)] = areas[0]
            areas = [0]

print(f'Total areas found: {len(final_info)}')
final_info = {k: v for k, v in sorted(final_info.items(), key=lambda x: -x[1])}
n = 0
for key, value in final_info.items():
    n += 1
    print(f'Area #{n} at {key}, size: {value}')
