#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

int_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

duo_list = []
for number in int_list:
    if number % 2 == 0:
        duo_list.append(number)
sum_list = sum(duo_list)
print("сумма усіх ПАРНИХ чисел в цьому лісті ",sum_list)



