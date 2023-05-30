names = ['sue', 'suzzie', 'suzzana', 'susan', 'suez']

print(names[1:])
print(names)

numbers = [3, 6, 2, 8, 134, 4, 10, 1, 12]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)