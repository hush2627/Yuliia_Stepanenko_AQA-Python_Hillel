def sum_string_numbers(text):
    numbers = text.split(",")
    total = 0
    for num in numbers:
        total = total + int(num)
    return total


data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    try:
        result = sum_string_numbers(item)
        print(result)
    except:
        print("Не можу це зробити!")