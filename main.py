import time
import os
from address_book import main as address_book
from notes import main as notes
from sorter import main as sorter
from abc import ABC, abstractmethod

class BaseView(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def handle_command(self, command):
        pass

class ConsoleView(BaseView):

    def display(self):
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

    def handle_command(self, command):
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

def main():
    console_view = ConsoleView()

    while True:
        console_view.display()
        command = input("Введіть ваше значення: ")

        if command == "4":
            print("Допобачення!")
            time.sleep(2)
            os.system('cls')
            break

        console_view.handle_command(command)

if __name__ == "__main__":
    main()
