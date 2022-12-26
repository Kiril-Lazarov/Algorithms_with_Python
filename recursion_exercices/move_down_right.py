n = int(input())
m = int(input())

grid = []
buffer = []
for i in range(n):
    for j in range(m):
        buffer.append('*')
    grid.append(buffer)
    buffer = []
grid[0][0] = 'M'

number_of_paths = [0]


def move_right(col):
    if col + 1 < m:
        return col + 1
    return None


def move_down(row):
    if row + 1 < n:
        return row + 1
    return None


def marinette_move(row, col, number_of_paths):
    if row == n - 1 and col == m - 1:
        number_of_paths[0] += 1
        return
    new_col = move_right(col)
    if new_col is not None:
        if grid[row][new_col] == '*':
            grid[row][new_col] = 'V'
            marinette_move(row, new_col, number_of_paths)
            grid[row][new_col] = '*'
    new_rol = move_down(row)
    if new_rol is not None:
        if grid[new_rol][col] == '*':
            grid[new_rol][col] = 'V'
            marinette_move(new_rol, col, number_of_paths)
            grid[new_rol][col] = '*'


marinette_move(0, 0, number_of_paths)
print(number_of_paths[0])
