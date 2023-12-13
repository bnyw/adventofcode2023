# Part 1
# with open("4/input.txt", "r", encoding="utf-8") as file:
#     scans = file.readlines()

# total = 0
# for line in scans:
#     score = 0
#     line = line.replace("  ", " ")
#     winning = line.split("|")[0].split(":")[1].strip().split(" ")
#     have = line.split("|")[1].strip().split(" ")

#     for n in have:
#         if n in winning:
#             if score == 0:
#                 score += 1
#             else:
#                 score *= 2
#     total += score

# print(total)

# Part 2
with open("4/input.txt", "r", encoding="utf-8") as file:
    scans = file.readlines()

total = 0
journal = {}
for line in scans:
    score = 0
    line = line.replace("  ", " ")
    card_id = line.split("|")[0].split(":")[0].split(" ")[-1]
    winning = line.split("|")[0].split(":")[1].strip().split(" ")
    have = line.split("|")[1].strip().split(" ")

    try:
        journal[card_id] += 1
    except:
        journal[card_id] = 1

    for n in have:
        if n in winning:
            score += 1
    if score != 0:
        for i in range(int(card_id) + 1, int(card_id) + int(score) + 1, 1):
            try:
                journal[str(i)] += journal[card_id]
            except:
                journal[str(i)] = journal[card_id]

    total = sum(journal.values())

print(total)
