# Давлатов Юсуфхон
# Промежуточная Контрольная работа #1
# Задача 1.17: Среди трех чисел найти среднее, если есть одинаковое число, вывести сообщение ошибка

# Комментарии: Я тут использую кортежи(tuple) для хранения данных потомучто у нас определенное количество значений


def get_numbers():
    """
    Запрашивает у пользователя три числа
    :return: Кортеж из трех чисел или None при ошибке
    """
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        c = float(input("Введите третье число: "))
    except ValueError:
        print("Пожалуйста, вводите числа!")
        return

    return a, b, c


def check_numbers(numbers: tuple):
    """
    Проверяет список чисел на повторяющиеся значения
    :param numbers: Кортеж состоящий из трех чисел с плавающей точкой
    :return: Кортеж из трех чисел или None при ошибке
    """
    if len(numbers) == len(set(numbers)):
        return numbers
    else:
        print("Вы ввели 2 или более одинаковых значений")


def average(numbers: tuple) -> float:
    """
    Вычисляет и возвращает значение чисел кортежа
    :param numbers: Кортеж состоящий из трех чисел с плавающей точкой
    :return: Среднее значение чисел из кортежа
    """
    avg = 0
    for number in numbers:
        avg += number
    avg /= len(numbers)
    return avg


def main():
    print("Программа для нахождения среднего значения из трех чисел!")
    nums = get_numbers()

    if nums is not None:
        chk_nums = check_numbers(nums)
    else:
        chk_nums = None

    if chk_nums is not None:
        print("Среднее значение введенных вами чисел =", average(chk_nums))


if __name__ == "__main__":
    main()
