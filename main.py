import time
import os
from personal_assistant.address_book import main as address_book
from personal_assistant.notes import main as notes
from personal_assistant.sorter import main as sorter


class Main:
    def show_all():
        while True:
            print("1. Адресна книга")
            print("2. Нотатки")
            print("3. Сортування файлів")
            print("4. Вихід")

            command = input("Введіть ваше значення: ")

            if command == "1":
                os.system('cls')
                address_book()

            elif command == "2":
                os.system('cls')
                notes()

            elif command == "3":
                os.system('cls')
                sorter()

            elif command == "4":
                print("Допобачення!")
                time.sleep(2)
                os.system('cls')
                break

            else:
                print("Некорректне значення, спробуйте ще раз")

if __name__ == "__main__":
    Main.show_all()
