# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер четверти от 1 до 4 включительно"))
if a == 1:
    print("x(0, infinity), y(0, infinity)")
elif a == 2:
    print("x(- infinity, 0), y(0, infinity)")
elif a == 3:
    print("x(- infinity, 0), y(- infinity, 0)")
elif a == 4:
    print("x(0, infinity), y(- infinity, 0)")
else:
    print("неверный ввод")



