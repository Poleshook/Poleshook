from time import sleep
print("Здравствуйте")
sleep(1)
first = int(input("Введите пожалуйста первое целое число из трёх: "))
second = int(input("Введите пожалуйста второе целое число из трёх: "))
third = int(input("Введите пожалуйста третье целое число из трёх: "))
if first == second == third:
    print("3")
elif first != second and first != third and second != third:
    print("0")
else:
    print("2")
