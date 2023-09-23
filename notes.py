import time
import os
import pickle

class NoteBook:
    def __init__(self):
        super().__init__()
        self.notes = []

    def edit(self, note):
        """
        Редагувати нотатку в блокноті.
        """
        index = self.notes.index(note)
        print(f"Тег:\n{note.tag}")
        new_tag = input(f"Введіть новий значення тегу: ") or note.tag
        os.system('cls')
        print(f"Ваша нотатка:\n{note.content}")
        new_content = input(f"Введіть новий текст: ") or note.content
        os.system('cls')
        self.notes[index] = NoteTag(new_tag, new_content)
        print(f"Нотатка '{note.tag}' відредагована.")

    def delete(self, note):
        """
        Видалити нотатку з блокнота.
        """
        self.notes.remove(note)
        print(f"Нотатка '{note.tag}' видалена.")

    def save(self):
        """
        Зберегти нову нотатку в блокнот.
        """
        tag = input("Введіть тег для нотатки: ")
        while tag == '':
            print('Тег не може бути пустим')
            tag = input("Введіть тег для нотатки: ")

        content = input("Введіть зміст для нотатки: ")
        while content == '':
            print('Зміст може бути пустим')
            content = input("Введіть зміст для нотатки: ")
        new_note = NoteTag(tag, content)
        self.notes.append(new_note)
        print(f"Нотатка '{tag}' додана.")

    def view(self):
        """
        Переглянути всі нотатки в блокноті.
        """
        if not self.notes:
            print("Немає доступних нотаток.")
        else:
            print(f"|{'№':^5}|{'Тег':^120}|")
            for index, note in enumerate(self.notes, start=1):
                parts = [note.content[i:i + 120] for i in range(0, len(note.content), 120)]
                print(f"|{index:^5}|{note.tag:^120}|")
                for part in parts:
                    print(f"|{'':^5}|{part:^120}|")
                print()

    def sort(self):
        """
        Сортувати всі нотатки в блокноті.
        """
        self.notes.sort(key=lambda note: note.tag)
        self.view()
        print("Нотатки відсортовані.")

    def search(self, keyword):
        """
        Пошук нотаток за конкретним ключовим словом в блокноті.
        """
        matching_notes = [note for note in self.notes if keyword in note.tag or keyword in note.content]
        if matching_notes:
            os.system('cls')
            print(f"|{'№':^5}|{'Тег та нотатка':^120}|")
            for index, note in enumerate(matching_notes, start=1):
                parts = [note.content[i:i + 120] for i in range(0, len(note.content), 120)]
                print(f"|{index:^5}|{note.tag:^120}|")
                for part in parts:
                    print(f"|{'':^5}|{part:^120}|")
                print()

        else:
            os.system('cls')
            print("Не знайдено нотаток за вказаним ключовим словом.")

    def save_to_file(self, filename):
        # Отримуємо абсолютний шлях до кореневого каталогу пакету
        package_root = os.path.abspath(os.path.dirname(__file__))

        # Формуємо абсолютний шлях до каталогу 'notes_save'
        save_directory = os.path.join(package_root, 'notes_save')

        # Перевіряємо, чи існує каталог 'notes_save'
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)  # Якщо не існує, створюємо його

        with open(f'{save_directory}/{filename}', 'wb') as file:
            pickle.dump(self.notes, file)

    def load_from_file(self, filename):
        package_root = os.path.abspath(os.path.dirname(__file__))
        load_directory = os.path.join(package_root, 'notes_save')

        with open(f'{load_directory}/{filename}', 'rb') as file:
            self.notes = pickle.load(file)


class NoteTag:
    def __init__(self, tag, content):
        self.tag = tag
        self.content = content


def main():
    notebook = NoteBook()

    while True:
        print("1. Додати нову нотатку")
        print("2. Редагувати нотатку")
        print("3. Видалити нотатку")
        print("4. Переглянути всі нотатки")
        print("5. Сортувати всі нотатки")
        print("6. Пошук нотатки")
        print("7. Зберегти нотатки в файл")
        print("8. Завантажити нотатки з файлу")
        print("9. Вихід")
        command = input("Введіть ваше значення: ")

        if command == "1":
            os.system('cls')
            notebook.save()
            time.sleep(2)
            os.system('cls')

        elif command == "2":
            os.system('cls')
            notebook.view()
            if notebook.notes:
                try:
                    index = int(input("Введіть номер нотатки для редагування: ")) - 1
                    if 0 <= index < len(notebook.notes):
                        notebook.edit(notebook.notes[index])
                except:
                    print('Некорректне значення')
                    time.sleep(2)
                    os.system('cls')


        elif command == "3":
            os.system('cls')
            notebook.view()
            if notebook.notes:
                index = int(input("Введіть номер нотатки для видалення: ")) - 1
                if 0 <= index < len(notebook.notes):
                    notebook.delete(notebook.notes[index])
                else:
                    print('Некорректне значення')
                    time.sleep(2)
                    os.system('cls')

        elif command == "4":
            os.system('cls')
            notebook.view()
            input('Для повернення натисніть Ентер')
            os.system('cls')

        elif command == "5":
            os.system('cls')
            option = input(
                "Всі нотатки будуть відсортовані в алфавітному порядку. Відсортувати? (так/ні): ").strip().lower()

            if option == "так":
                notebook.sort()
                time.sleep(2)
                os.system('cls')
            elif option == "ні":
                print('Відміна')
                time.sleep(2)
                os.system('cls')
            else:
                print('Некорректне значення, повернення до годовного меню')
                time.sleep(2)
                os.system('cls')


        elif command == "6":
            os.system('cls')
            keyword = input("Введіть ключове слово для пошуку: ")
            notebook.search(keyword)
            input('Для повернення натисніть Ентер')
            os.system('cls')

        elif command == '7':
            os.system('cls')
            filename = input("Введіть назву файлу для збереження: ")
            if filename != '':
                notebook.save_to_file(filename)
                print("Дані збережено")
                time.sleep(2)
                os.system('cls')
            else:
                print('Імя файлу не може бути пустим')
                time.sleep(2)
                os.system('cls')

        elif command == '8':
            os.system('cls')
            filename = input("Введіть назву файлу для завантаження: ")
            try:
                notebook.load_from_file(filename)
                print("Дані завантажено")
                time.sleep(2)
                os.system('cls')
            except:
                print("Файл не знайдено")
                time.sleep(2)
                os.system('cls')

        elif command == "9":
            os.system('cls')
            break

        else:
            print("Некоректна команда. Спробуйте ще раз.")
            time.sleep(2)
            os.system('cls')


if __name__ == "__main__":
    main()
