n = int(input())
m = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))

visited = []


def moves(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


moves_sequence = ['up', 'down', 'left', 'right']

letters_dict = {}


def dfs(row, col, letter):
    if (row, col) not in visited:
        visited.append((row, col))
        for direction in moves_sequence:
            new_row, new_col = moves(row, col, direction)
            if 0 <= new_row < n and 0 <= new_col < m:

                if matrix[new_row][new_col] == letter:
                    dfs(new_row, new_col, letter)


for row in range(n):
    for col in range(m):
        if (row, col) not in visited:
            letter = matrix[row][col]

            dfs(row, col, letter)
            if letter not in letters_dict:
                letters_dict[letter] = 0
            letters_dict[letter] += 1
sorted_dict = {k:v for k,v in sorted(letters_dict.items())}
total = sum(list(sorted_dict.values()))
print(f'Areas: {total}')
for letter, number in sorted_dict.items():
    print(f"Letter '{letter}' -> {number}")
