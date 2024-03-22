# Your task, is to create N×N multiplication table, of size provided in parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]


# def multiplication_table(size):
#     result = []
#     for i in range(1, size + 1):
#         row = []
#         for j in range(1, size + 1):
#             print(f'{i}x{j}={j * i}')
#             row.append(j * i)
#         result.append(row)
#     return result


def multiplication_table(size):
    # [[inner_variable * outer_variable for inner_variable in inner_range] for outer_variable in outer_range]
    result = [[x * y for x in range(1, size + 1)] for y in range(1, size + 1)]
    return result


print(multiplication_table(3))

# comprehension
num_rows = 3
num_cols = 4
table = [[row_idx * col_idx for col_idx in range(1, num_cols + 1)] for row_idx in range(1, num_rows + 1)]
# row_idx is the “outer” variable, and col_idx is the “inner” variable.
# range(1, num_rows + 1) is the “outer” range, and range(1, num_cols + 1) is the “inner” range.
# row_idx * col_idx is the operation performed in the inner loop.


# loop
num_rows = 3
num_cols = 4
table = []
for row_idx in range(1, num_rows + 1):  # outer loop
    row = []
    for col_idx in range(1, num_cols + 1):  # inner loop
        row.append(row_idx * col_idx)  # operation performed in the inner loop
    table.append(row)

# The first (outer) loop iterates over row_idx in range(1, num_rows + 1).
# The second (inner) loop iterates over col_idx in range(1, num_cols + 1).
# The operation row_idx * col_idx is performed in the inner loop, and the result is appended to the row list.
# After the inner loop finishes, the row list (which now contains the results of the inner loop) is appended to the table list.
