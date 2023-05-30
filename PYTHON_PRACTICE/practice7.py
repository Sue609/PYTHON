numbers = [2, 3, 1, 5, 2, 7, 3, 1, 2, 9, 0, 1, 2]
dups = []

for number in numbers:
    if number not in dups:
        dups.append(number)
print(dups)