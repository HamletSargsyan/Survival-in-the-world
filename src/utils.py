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


def format_list(input_list: list, num_columns: int):
    # Определяем максимальные длины строк для каждого столбца
    max_lens = [0] * num_columns
    for i in range(len(input_list)):
        col_index = i % num_columns
        max_lens[col_index] = max(max_lens[col_index], len(input_list[i]))

    # Формируем отформатированные строки
    formatted_lines = []
    for i in range(0, len(input_list), num_columns):
        row_items = input_list[i : i + num_columns]
        formatted_line = " | ".join(
            f"{item:<{max_lens[j]}}" for j, item in enumerate(row_items)
        )
        formatted_lines.append(formatted_line)

    return "\n".join(formatted_lines)
