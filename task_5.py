# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from random import randint
from typing import Callable


def fun_decor(fun: Callable) -> Callable[[int, int], None]:
    def wrapper(*args):
        num, count = args
        if num not in range(1, 101) and count not in range(1, 11):
            return fun(randint(1, 100), randint(1, 10))
        elif num in range(1, 101) and count not in range(1, 11):
            return fun(num, randint(1, 10))
        elif num not in range(1, 101) and count in range(1, 11):
            return fun(randint(1, 100), count)
        else:
            return fun(num, count)

    return wrapper


@fun_decor
def fun_secret(num: int, count: int):
    current_num = randint(1, num)
    for item in range(1, count + 1):
        spam = int(input(f'Введите число в диапазоне от 1 до {num} (попытка № – {item}): \n'))
        if spam == current_num:
            print('Верно')
            break
        elif spam > current_num:
            print('Меньше')
        else:
            print('Больше')


if __name__ == '__main__':
    fun_secret(50, 8)
