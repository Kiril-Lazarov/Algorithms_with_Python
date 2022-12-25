n = int(input())
m = int(input())

matrix = [[char for char in input()] for rows in range(n)]
start_row, start_col = 0, 0
visit_cells = []
steps = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}
dir_list = ['L', 'R', 'U', 'D']


def get_next_position(rows, cols, direction):
    if direction == 'U':
        return rows - 1, cols
    elif direction == 'D':
        return rows + 1, cols
    elif direction == 'L':
        return rows, cols - 1
    elif direction == 'R':
        return rows, cols + 1


def move(row, col, matrix, visit_cells):
    for direction in dir_list:
        next_row, next_col = get_next_position(row, col, direction)
        if 0 <= next_row < n and 0 <= next_col < m:
            if matrix[next_row][next_col] == '-':
                visit_cells.append(direction)
                matrix[row][col] = 'v'
                move(next_row, next_col, matrix, visit_cells)
                matrix[next_row][next_col] = '-'
                visit_cells.pop()
            if matrix[next_row][next_col] == 'e':
                visit_cells.append(direction)
                print(''.join(visit_cells))
                visit_cells.pop()

                return


move(start_row, start_col, matrix, visit_cells)
