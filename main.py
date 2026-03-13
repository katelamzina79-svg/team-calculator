# main.py - Основная программа

import config
from utils import add, subtract, multiply, divide

def print_header():
    print(config.COLORS['info'] + "=" * 50 + config.COLORS['reset'])
    print(f"{config.APP_NAME} v{config.VERSION}")
    print("=" * 50)
    print(f"Авторы: {', '.join(config.AUTHORS)}")
    print("=" * 50)

def print_menu():
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

def get_numbers():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return a, b
    except ValueError:
        print(config.COLORS['error'] + "Ошибка: введите числа!" + config.COLORS['reset'])
        return None, None

def main():
    print_header()
    
    while True:
        print_menu()
        choice = input("Ваш выбор: ")
        
        if choice == '5':
            print(config.COLORS['success'] + "До свидания!" + config.COLORS['reset'])
            break
        
        if choice not in ['1', '2', '3', '4']:
            print(config.COLORS['error'] + "Неверный выбор!" + config.COLORS['reset'])
            continue
        
        a, b = get_numbers()
        if a is None:
            continue
        
        try:
            if choice == '1':
                result = add(a, b)
                op = "+"
            elif choice == '2':
                result = subtract(a, b)
                op = "-"
            elif choice == '3':
                result = multiply(a, b)
                op = "*"
            elif choice == '4':
                result = divide(a, b)
                op = "/"
            
            print(config.COLORS['success'] + f"\nРезультат: {a} {op} {b} = {result}" + config.COLORS['reset'])
            
        except ValueError as e:
            print(config.COLORS['error'] + f"Ошибка: {e}" + config.COLORS['reset'])
        except Exception as e:
            print(config.COLORS['error'] + f"Неизвестная ошибка: {e}" + config.COLORS['reset'])

if __name__ == "__main__":
    main()
