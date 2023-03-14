# Модуль random для генерирования псевдослучайных чисел
import random

# random.random() - генерация случайного числа от 0.0 до 1.1
number = random.random()
print(number)

# random.randint() - генерация целого случайного числа в диапазоне
number = random.randint(5, 10)
print(number)

# random.randrange() - генерация целого случайного числа из набора чисел
number = random.randrange(10, 100, 5)
print(number)

# random uniform() - генерация вещественного числа в промежутке
number = random.uniform(2.3, 7.8)
print(number)


# Модуль random для работы со временем
import time

# time.time() - время в секундах от 1 января 1970 года 00:00:00
seconds = time.time()
print(seconds)

# time.ctime() - перевод на местное время, в привычный для человека вид
seconds = time.ctime(time.time())
print(seconds)

# time.sleep() - остановка выполнения программы в секундах
print("Старт!")
seconds = time.sleep(2)
print("Финиш!")
