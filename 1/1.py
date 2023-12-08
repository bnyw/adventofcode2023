# Part 1
# with open("1/input.txt", "r", encoding="utf-8") as file:
#     scans = file.readlines()

# total = 0
# for line in scans:
#     lineList = list(line)
#     n = ''
#     for c in lineList:
#         if c.isdigit():
#             n += c
#             break
#     lineList.reverse()
#     for c in lineList:
#         if c.isdigit():
#             n += c
#             break
#     total += int(n)

# print(total)


# Part 2
digit_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def ltr_replace(text: str) -> str:
    replaced = False
    for dig in digit_word:
        if text.startswith(dig):
            text = text.replace(dig, str(digit_word.index(dig) + 1), 1)
            replaced = True
            if len(text) > 2:
                text = text[0] + ltr_replace(text[1:])

    if not replaced and len(text) > 2:
        text = text[0] + ltr_replace(text[1:])

    return text


with open("1/input.txt", "r", encoding="utf-8") as file:
    scans = file.readlines()

total = 0
for line in scans:
    line = ltr_replace(line)
    backup = line

    lineList = list(line)
    n = ""
    for c in lineList:
        if c.isdigit():
            n += c
            break
    lineList.reverse()
    for c in lineList:
        if c.isdigit():
            n += c
            break
    total += int(n)

print(total)
