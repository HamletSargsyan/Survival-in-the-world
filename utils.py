import os
import sys
import tty
import termios


def clear():
    os.system("clear")


def wait_for_keypress():
    print("Нажмите любую клавишу, чтобы продолжить...")
    
    # Сохраняем текущие настройки терминала
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        # Устанавливаем неблокирующий режим ввода
        tty.setcbreak(sys.stdin.fileno())

        # Ждем нажатия клавиши
        sys.stdin.read(1)
    finally:
        # Восстанавливаем настройки терминала
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
