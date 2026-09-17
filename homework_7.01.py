# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
"""
from turtledemo.chaos import line
from unittest import result


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier

        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

digit_one = 5
digit_two = 5

def sum_digits(digit_one, digit_two):
    result = digit_one + digit_two
    return result
print("сумма:   ", sum_digits(digit_one, digit_two))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
digits_list = [3,5,8,12]
def sum_average (digits_list):
    result = sum(digits_list)/len(digits_list)
    return result

print("середнє арифметичне списку чисел:   ", sum_average(digits_list))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def text_string (text):
    result = text [::-1]
    return result

print("рядок :", text_string("How hard it is!!!"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
long_text = ["Olga", "it", "conversation", "two"]

def longest_word(long_text):
    long = long_text[0]

    for word in long_text:
        if len(word) > len(long):
            long = word

    return long

print("найдовше слово у списку:", longest_word(long_text))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.

#computer_price = 18 * 1179
#print("вартість комп’ютера = ", computer_price,"грн")

payment_time = 18
month_payment = 1179
def computer_price (payment_time, month_payment):
    price = payment_time * month_payment
    return price
print("вартість комп’ютера = ", computer_price(payment_time,month_payment), "грн")

# task 8
#Напишіть цикл, який буде вимагати від користувача ввести слово,в якому є літера "h" (враховуються як великі так і маленькі).
#Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def check_word():
    while True:
        word = input("Введіть слово з літерою h/H: ")

        if "h" in word or "H" in word:
            return word

print("Введено правильне слово:", check_word())
# task 9
#Іринка, готуючись до свого дня народження, склала список того,
#що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
#для даного її замовлення.
#Назва товару    Кількість   Ціна
#Піца велика     4           274 грн
#Піца середня    2           218 грн
#Сік             4           35 грн
#Торт            1           350 грн
#Вода            3           21 грн
def order_price ():
    pizza_big = 4*274
    pizza_middle = 2 * 218
    juice = 4 * 35
    cake = 350
    water = 3 * 21
    total_money = sum([pizza_big, pizza_middle, juice, cake, water])
    return total_money

print("скільки грошей знадобиться для замовлення: ",order_price(),"грн")
#task 10
#Ігор займається фотографією. Він вирішив зібрати всі свої 232
#фотографії та вклеїти в альбом. На одній сторінці може бути
#розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
#Ігорю, щоб вклеїти всі фото?
def photo_pages():
    all_photos = 232
    photos_per_page = 8
    pages_quantity = all_photos//photos_per_page
    return  pages_quantity

print("Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото: ", photo_pages())