"""D:/Загрузки/Практическая работа 5 - Разработка документации.pdf"""
from termcolor import colored, cprint


def number_control(name_of_p, min_val=-1e8, max_val=1e8):
    """
    Проверка корректности вводимых чисел

    Функция запрашивает число у пользователя до тех пор,
    пока оно не будет целым и не будет принадлежать отрезку
    [min_val; max_val].
    Функция принимает на вход три параметра:
    1) Строку, которая будет выводиться на экран.
    По ней пользователь должен понять, какую роль запрашиваемое число несет в программе.
    2) Число, минимальное значение числа, которое вводит пользователь
    3) Число, максимальное значение числа, которое вводит пользователь

    Args:
        name_of_p (str): название переменной
        min_number (int, optional): минимальное допустимое значение. Defaults to -1e8.
        max_number (int, optional): максимальное допустимое значение. Defaults to 1e8.

    Returns:
        int: число, которое ввел пользователь, прошедшее проверку

    Examples:
        >>> number_control("N", 0, 3)
        Input the number: N = 10
        It should be an integer from 0 to 3
        try again...
        Input the number: N = 2.2
        It should be an integer from 0 to 3
        try again...
        Input the number: N = 3
        3
    """
    while True:
        input_val = input(
            colored("Input the number: " + name_of_p + " = ", 'green'))

        try:
            input_val = int(input_val)

            if min_val <= input_val <= max_val:
                return input_val

            raise ValueError

        except ValueError:
            cprint(f"It should be an integer from {min_val} to {max_val}", 'red')

        print("try again...")


def syracuse_sequence(n):
    """
    Вычисление сиракузской последовательности

    Функция вычисляет сиракузскую последовательность по заданному числу.
    В работает по рекурсивному алгоритму, условием завершения которого,
    является значение равное 1. Функция на каждом шаге увеличивает возвращаемый
    список, на одно значение - следующее число последовательности.

    Args:
        n (int): натуральное число по которому вычисляется последовательность

    Returns:
        list: сиракузская последовательность

    Examples:
        >>> syracuse_sequence(1)
        [1, 4, 2, 1]
        >>> syracuse_sequence(3)
        [3, 10, 5, 16, 8, 4, 2, 1]
    """
    next_n_func = lambda a: a // 2 if a % 2 == 0 else a * 3 + 1
    if next_n_func(n) == 1:
        return [n, 1]
    return [n, *syracuse_sequence(next_n_func(n))]


def syracuse_max(n):
    """
    Нахождение наибольшего числа в сиракузской последовательности

    Функция вычислет наибольшее число последовательности,
    заданной числом n. Сначала вычисляется сама последовательность
    с помощью функции syracuse_sequence(*args). После чего записанная
    последовательность сортируется по возрастанию, и берется самый правый
    элемент (наибольший).

    Args:
        n (int): натуральное число по которому вычисляется последовательность

    Returns:
        int: наибольшее число последоватлельности

    Examples:
    >>> syracuse_max(1)
    4
    >>> syracuse_max(3)
    16
    """
    sequence = syracuse_sequence(n)
    sequence.sort()
    return sequence[-1]


def main():
    """main"""
    N = number_control("N", 1)

    mas = syracuse_sequence(N)
    print(mas)

    max_el = syracuse_max(N)
    print(max_el)

if __name__ == '__main__':
    main()
