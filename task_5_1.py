### 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

def odd_nums(number):
    for i in range(0, number + 1, 1):
        if i % 2 == 1:
            yield i


odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

