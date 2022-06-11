# Библиотеки/файлы
from process_frames import print_frames  # Файл с функцией по выводу кадров
from colorama import Fore  # Библиотека с помощью которой будем менять цвет в терминале
import sys  # Аргументы

# Список цветов
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
pink = Fore.MAGENTA
yellow = Fore.YELLOW
cyan = Fore.CYAN
white = Fore.WHITE
RESET = Fore.RESET  # Дефолтный цвет

try:
    if sys.argv[1] == "-r":
        print_frames(color=red)
    elif sys.argv == "-g":
        print_frames(color=green)
    elif sys.argv[1] == "-b":
        print_frames(color=blue)
    elif sys.argv[1] == "-p":
        print_frames(color=pink)
    elif sys.argv[1] == "-y":
        print_frames(color=yellow)
    elif sys.argv[1] == "-c":
        print_frames(color=cyan)
    elif sys.argv[1] == "-w":
        print_frames(color=white)
    elif sys.argv[1] == "--help":  # Помощь
        print("Танцующий ASCII дед инсайд кот.\nДля использования введите команду zxc + цвет, который вы хотите использовать\nДоступные цвета:\n - r - красный\n - g - зеленый\n - b - синий\n - p - розовый \n - y - желтый\n - c - голубой\n - w - белый")
except IndexError:
    print("Вы не ввели аргумент!\nДля помощи введите zxc --help/zxc.py --help")
except KeyboardInterrupt:
    print(RESET + "Пока!)")
except:
    pass  # ПХАХАХАХАХАХАХАХАХХ

