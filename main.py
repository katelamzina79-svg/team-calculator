# main.py - Основная программа

import config

def print_header():
    print("=" * 50)
    print(f"{config.APP_NAME} v{config.VERSION}")
    print("=" * 50)
    print(f"Авторы: {', '.join(config.AUTHORS)}")
    print("=" * 50)

def main():
    print_header()
    print("Калькулятор в разработке...")
    print("Скоро здесь появится меню!")

if __name__ == "__main__":
    main()