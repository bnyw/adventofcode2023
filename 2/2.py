# Part 1
# with open("2/input.txt", "r", encoding="utf-8") as file:
#     scans = file.readlines()

# setting = {"red": 12, "green": 13, "blue": 14}

# total = 0
# for line in scans:
#     id = line.split(":")[0].split(" ")[1]
#     samples = line.split(":")[1].split(";")

#     valid = True

#     for sample in samples:
#         cubes = sample.lstrip().rstrip().split(", ")
#         for cube in cubes:
#             amount, color = cube.split(" ")
#             if int(amount) > setting[color]:
#                 valid = False

#     if valid:
#         total += int(id)

# print(total)


# Part 2
with open("2/input.txt", "r", encoding="utf-8") as file:
    scans = file.readlines()

total = 0
for line in scans:
    minimum_cube = {"red": 0, "green": 0, "blue": 0}
    id = line.split(":")[0].split(" ")[1]
    samples = line.split(":")[1].split(";")

    for sample in samples:
        cubes = sample.lstrip().rstrip().split(", ")
        for cube in cubes:
            amount, color = cube.split(" ")
            if int(amount) > minimum_cube[color]:
                minimum_cube[color] = int(amount)

    total += minimum_cube["red"] * minimum_cube["green"] * minimum_cube["blue"]

print(total)
