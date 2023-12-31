# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable
from random import randrange


def main(func: Callable):
    def wrappers():
        count = 0
        result = func()
        while not result:
            count += 1
            result = func()
        return count

    return wrappers


@main
def rand_num():
    f = randrange(0, 501)
    if f == 10:
        return True
    else:
        return False


print(f'Функция {rand_num.__name__} отработала {rand_num()} раз(а)')
