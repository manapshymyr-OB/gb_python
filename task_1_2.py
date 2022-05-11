"""2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):"""

number_list = []

for i in range(1, 1001, 2):
    cube = i ** 3
    number_list.append(cube)


def sum_digits(digits):
    digits_sum = 0

    while digits != 0:

        digits_sum += digits % 10
        digits //= 10

    return digits_sum

for i in number_list:

    digits_sum = sum_digits(i)
    digits_sum_with_seventeen = sum_digits(i + 17)
    if digits_sum % 7 == 0:
        print("Summa: %d" % digits_sum)
        print("Cube: %d" % i)
        pass
    if digits_sum_with_seventeen % 7 == 0:
        print("Summa i + 17: %d" % digits_sum_with_seventeen)
        print("Cube i + 17: %d" % i)