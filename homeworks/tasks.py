# for number in range(2, 21, 1):
#     if number % 2 == 0:
#         print(number)

# for number in range(0, 51):
#     if number % 2 == 0 or number % 3 == 0:
#         print(number)

# for number in range(0, 100):
#     if number % 2 == 0 and number % 5 == 0 or number % 7 == 0:
#         print(number)

# counts = 0
# for vovel in 'programming':
#     if vovel in "aeiou":
#         counts = counts + 1
#         print(counts)

# vovels = 0
# consonants = 0
# for vovel in 'developer':
#     if vovel in 'aeiou':
#         vovels = vovels + 1
#     else:
#         consonants = consonants + 1
#
# print(f"vovels = {vovels} \nconsonants = {consonants}")

# i = "Python3 is cool in 2025!"
# counts = 0
# for number in i:
#     if number.isdigit():
#         counts = counts + 1
#
# print(counts)

# total = 0
# for numbers in range(0, 51):
#     total += numbers
#
# print(total)

# total = 0
# for number in range (51):
#     if number % 2 != 0:
#         total += number
#
# print(total)

# counts = {}
# for letter in 'banana':
#     if letter in counts:
#         counts[letter] += 1
#     else:
#         counts[letter] = 1
#
# print(counts)

word = input('Enter your word: ')
counts = {}

for letter in word.lower():
    if letter.isalpha():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

print(f'{word}, letters = {counts}')