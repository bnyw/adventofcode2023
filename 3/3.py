import numpy as np


# Part 1

# n_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# ignore_list = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# def there_is_symbol(arr):
#     for i in arr:
#         if i not in ignore_list:
#             return True
#     return False

# with open("3/input.txt", "r", encoding="utf-8") as file:
#     scans = file.read().split("\n")

# n_row = len(scans)
# n_col = len(list(scans[0]))
# total = 0

# # for line in scans:
# for idx in range(len(scans)):
#     scans[idx] = list(scans[idx])

# np_line = np.array(scans)
# np_line_padded = np.pad(np_line, 1, "constant", constant_values=(".", "."))

# startIdx = (None, None)
# stopIdx = (None, None)
# for r in range(0, n_row + 2, 1):
#     for c in range(0, n_col + 2, 1):
#         if np_line_padded[r][c] in n_list:
#             if startIdx == (None, None):
#                 startIdx = (r, c)
#             else:
#                 stopIdx = (r, c)
#             continue
#         elif startIdx == (None, None):
#             continue
#         else:
#             if stopIdx == (None, None):
#                 stopIdx = (r, c - 1)
#             stride = np_line_padded[
#                 (startIdx[0] - 1) : (stopIdx[0] + 2),
#                 (startIdx[1] - 1) : (stopIdx[1] + 2),
#             ]
#             number = np_line_padded[r][startIdx[1] : stopIdx[1] + 1]
#             # print(stride)
#             # print(number)
#             # print(startIdx, stopIdx, there_is_symbol(stride.flatten()))
#             if there_is_symbol(stride.flatten()):
#                 # print(int("".join(number)))
#                 total += int("".join(number))
#             startIdx = (None, None)
#             stopIdx = (None, None)

#     startIdx = (None, None)
#     stopIdx = (None, None)

# # print(np_line_padded)
# print(total)

# Part 2

n_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_list = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def there_is_number(arr):
    for i in arr:
        if i in number_list:
            return True
    return False


def num_dir(arr):
    for idx, c in enumerate(arr):
        if c not in number_list:
            arr[idx] = "."

    arr = "".join(arr)

    if arr.startswith("..."):
        return None
    elif arr.startswith(tuple(n_list)) and arr.endswith(".."):
        return [(0, -1)]
    elif arr.startswith(tuple(n_list)) and arr[1] in n_list and arr.endswith("."):
        return [(1, -1)]
    elif (
        arr.startswith(tuple(n_list))
        and arr[1] in n_list
        and arr.endswith(tuple(n_list))
    ):
        return [(0, 1)]
    elif arr.startswith(".") and arr[1] in n_list and arr.endswith(tuple(n_list)):
        return [(1, 1)]
    elif arr.startswith("..") and arr.endswith(tuple(n_list)):
        return [(2, 1)]
    elif (
        arr.startswith(tuple(n_list)) and arr[1] == "." and arr.endswith(tuple(n_list))
    ):
        return [(0, -1), (2, 1)]
    elif arr.startswith(".") and arr[1] in n_list and arr.endswith("."):
        return [(1, 1)]
    else:
        return None


def search_number(r, c, arr, scheme):
    global N
    nums = []
    next_r = r - 1
    for r_offset in range(3):
        line_str = np.copy(arr[r_offset])
        num_dir_result = num_dir(line_str)
        if num_dir_result is not None:
            for offset, dir in num_dir_result:
                num = []
                next_c = c - 1 + offset
                while scheme[next_r + r_offset, next_c] in n_list:
                    if dir == -1:
                        num.insert(0, scheme[next_r + r_offset, next_c])
                    else:
                        num.append(scheme[next_r + r_offset, next_c])
                    next_c += dir
                    if (next_c < 0) or (next_c > (n_col + 1)):
                        break
                nums.append(int("".join(num)))
    if len(nums) == 2:
        print(arr)
        print(nums)
        N += 1
        print(N)
        return nums[0] * nums[1]
    else:
        return 0


with open("3/input.txt", "r", encoding="utf-8") as file:
    scans = file.read().split("\n")

n_row = len(scans)
n_col = len(list(scans[0]))
total = 0
N = 0

# for line in scans:
for idx in range(len(scans)):
    scans[idx] = list(scans[idx])

np_line = np.array(scans)
np_line_padded = np.pad(np_line, 1, "constant", constant_values=(".", "."))

for r in range(0, n_row + 2, 1):
    for c in range(0, n_col + 2, 1):
        if np_line_padded[r][c] == "*":
            stride = np_line_padded[
                (r - 1) : (r + 2),
                (c - 1) : (c + 2),
            ]
            # print(stride)
            # print(r, c, there_is_number(stride.flatten()))
            if there_is_number(stride.flatten()):
                window = np_line_padded[
                    (r - 1) : (r + 2),
                    (c - 1) : (c + 2),
                ]
                total += search_number(r, c, stride, np_line_padded)
                # print(int("".join(number)))
                # total += int("".join(number))

print(np_line_padded)
print(total)
