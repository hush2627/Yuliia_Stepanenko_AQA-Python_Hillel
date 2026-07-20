# task 01 == Виправте синтаксичні помилки
#print("Hello", end = " ")
#    print("world!")
from operator import and_

#hw 01:
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
# = "Hello"
#world = "world"
#if True:
#print(f"{hello} {world}!")

#hw 02:
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
#for letter in "Hello world!":
#    print()

#hw 03:
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
#apples = 2
#banana = x

#hw 04:
apples = 2
banana = 2*4
banana_quantity = banana
print(f" {banana_quantity}")

# task 05 == виправте назви змінних
#1_storona = 1
#?torona_2 = 2
#сторона_3 = 3
#$torona_4 = 4

#hw 05:
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
#perimeter = ? + ? + ? + ?
#print()

#hw 06:
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(perimeter)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
#hw 07:
apples = 4
pearches = apples + 5
plums = apples - 2
total_trees = apples + pearches + plums
print("всього дерев посадили в саду:", total_trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
#hw:08
morning = 5
noon = morning - 10
evening = noon + 4
print("Яка температура надвечір:",evening)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
#hw 09:
total_boys = 24
total_girls = total_boys//2
today_presence = sum([total_boys-1, total_girls -2])
print("Скількі сьогодні дітей у театральному гуртку:", today_presence)


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
#hw 10:
book_1 = 8
book_2 = book_1 + 2
book_3 = book_1/2 + book_2/2
all_books_sum = sum([book_1, book_2, book_3])
print("Скільки будуть коштувати усі книги, якщо купити по одному примірнику:", all_books_sum)