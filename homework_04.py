adventures_of_tom_sawer = """\
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

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n"," ")
print(adventures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("...."," ")
print(adventures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawer = " ".join(adventures_of_tom_sawer.split())
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_quantity=adventures_of_tom_sawer.count("h")
print('скількі разів у тексті зустрічається літера "h":' ,h_quantity)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adventures_of_tom_sawer.split()
upper_words_quantity = 0
for word in words:
    if word[0].isupper():
        upper_words_quantity += 1
print("Кількість слів, що починаються з великої літери:", upper_words_quantity)

## task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_first =adventures_of_tom_sawer.find("Tom")
tom_second =adventures_of_tom_sawer.find("Tom", tom_first+1)
print("позиція, на якій слово Tom зустрічається вдруге:", tom_second)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(".")
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_four = adventures_of_tom_sawer_sentences [3].lower()
print(sentence_four)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Є речення, яке починається з 'By the time'")
        break
else:
    print("Немає речення, яке починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adventures_of_tom_sawer_sentences[-2]
words_quantity = len(last_sentence.split())
print(words_quantity)