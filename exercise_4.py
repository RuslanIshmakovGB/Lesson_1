Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.


n = int(input("Введите целое положительное число "))
max = n % 10
print(max)
while n >= 1:
 n = n // 10
 print(n)
 if n % 10 > max:
    print(n)
 print(max)
 max = n % 10
    print(max)
 elif n > 9:
 pass
print("Максимальное цифра в числе ", max)