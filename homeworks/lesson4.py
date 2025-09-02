


def filler():
    print('*****' * 10)
pass


adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('Task 1')
updated_value = adwentures_of_tom_sawer.replace("\n", " ")
print(updated_value)
filler()

# task 02 ==
""" Замініть .... на пробіл
"""
print('Task2')
updated_value2 = updated_value.replace("....", " ")
print(updated_value2)
filler()
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 3")
updated_value3 = updated_value2.replace("   ", " ")
print(updated_value3)
filler()

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 4")
count = 0
for letter in updated_value3:
    if letter in ("h"):
        count +=1

print(count)
filler()

words = updated_value3.lower().count('h')
print(words)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
uppercase = updated_value3.split()
print(uppercase)

words_count = 0
for upper in uppercase:
    if upper[0].isupper():
        words_count += 1

print(words_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_position = updated_value3.find('Tom', 2)
print(tom_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = updated_value3.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3])
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# if adwentures_of_tom_sawer_sentences:
print("Task 9")
for by_the_time in adwentures_of_tom_sawer_sentences:
    if by_the_time.startswith('By the time'):
        print('True,', by_the_time)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_split = last_sentence.split()
words_count2 = len(words_split)
print(last_sentence)
print(words_count2)