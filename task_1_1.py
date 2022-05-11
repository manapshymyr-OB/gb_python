### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек"""


while True:
    # z = input()

    duration = int(input("duration = "))

    day = duration // 86400
    hours = (duration - day * 86400) // 3600
    minutes = (duration -(day * 86400 +  hours * 3600)) // 60
    # minutes = (duration - hours * 3600) // 60
    seconds = duration - (day * 86400 + hours * 3600 + minutes * 60)

    if duration < 60:
        print(str(seconds) + " сек")

    elif 60 <= duration < 3600:
        print(str(minutes) + " мин " + str(seconds) + " сек")
    elif 3600 <= duration < 86400:
        print(str(hours) + " час " + str(minutes) + " мин " + str(seconds) + " сек")

    elif 86400 <= duration :
        print(str(day) + " дн " + str(hours) + " час " + str(minutes) + " мин " + str(seconds) + " сек")

