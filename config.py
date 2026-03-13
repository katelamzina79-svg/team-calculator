# config.py - Настройки приложения

APP_NAME = "Командный Калькулятор"
VERSION = "1.1.0"
AUTHORS = ["Капитан", "Участник2", "Участник3", "Участник4", "Участник5"]

# Для colorama (кросс-платформенные цвета)
from colorama import Fore, Style

COLORS = {
    'info': Fore.CYAN,
    'success': Fore.GREEN,
    'warning': Fore.YELLOW,
    'error': Fore.RED,
    'reset': Style.RESET_ALL
}
