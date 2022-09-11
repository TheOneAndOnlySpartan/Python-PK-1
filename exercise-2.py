# Давлатов Юсуфхон
# Промежуточная Контрольная работа #1
# Задача 2.7: Выведите список файлов в указанной директории (папки).

# Комментарии: Сделал красиво) Не надо вопросов, я сделал то что написано в задании
# Комментарии: Еще можно прописать путь сразу перед запуском программы через консоль, но цветокод тут уже ломается,
#              Не знаю как исправить

import os
import sys
from datetime import datetime
from colorama import Fore, Back, Style
from prettytable import PrettyTable

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date
def convert_size(size_bytes):
    mb = size_bytes / 1024
    gb = size_bytes / 1024 / 1024

    if mb < 0.6:
        size = f"{round(size_bytes, 2)} Байт"
    elif mb > 600:
        size = f"{round(gb, 2)} ГиБ"
    else:
        size = f"{round(mb, 2)} КиБ"

    return size

def get_files(path: str) -> list:
    """
    Возвращает все файлы которые находятся в директории path
    :param path: Путь к директории
    :return: Список из элементов файлов типа DirEntry
    """
    directory = os.scandir(path)
    return [files for files in directory if files.is_file()]

def get_folders(path: str):
    """
    Возвращает все директории которые находятся в директории path
    :param path: Путь к директории
    :return: Список из элементов директорий (папок) типа DirEntry
    """
    directory = os.scandir(path)
    return [folder for folder in directory if folder.is_dir()]

def main(dir_path: str):
    try:
        files = get_files(dir_path)
        folders = get_folders(dir_path)
    except FileNotFoundError:
        print("Введите правильный путь, например: C:\Windows")
        return


    table = PrettyTable(["Название", "Размер", "Обновлено"])
    table.align = "l"

    for folder in folders:
        stat = folder.stat()
        table.add_row([f"{Fore.GREEN}📁 {folder.name}{Fore.RESET}", "Папка", convert_date(stat.st_mtime)])

    for file in files:
        stat = file.stat()
        table.add_row([f"{Fore.CYAN}📄 {file.name}{Fore.RESET}", convert_size(stat.st_size), convert_date(stat.st_mtime)])

    print(table)


if __name__ == "__main__":
    print("Добро пожаловать в программу для просмотра директорий!")

    file_name = sys.argv[0]
    try:
        path = sys.argv[1]
    except IndexError:
        path = input("Введите путь к директории: ")

    main(path)
