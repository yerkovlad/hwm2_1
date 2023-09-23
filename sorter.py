import platform
import time
from pathlib import Path
import shutil
import os

# Словник розширень для кожного типу файлів
file_extensions = {
    'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
    'video': ['AVI', 'MP4', 'MOV', 'MKV'],
    'archives': ['ZIP', 'GZ', 'TAR'],
    'unknown': '',
}


def sort_files_recursive(source_path, destination_path):
    # Отримуємо об'єкт каталогу джерела
    source_directory = Path(source_path)

    # Ітеруємо всі файли та каталоги у вихідному каталозі
    for item in source_directory.iterdir():
        # Перевіряємо, чи ім'я елементу не знаходиться в списку розширень файлів або чи шлях не вказує на вихідний каталог
        if item.name not in file_extensions.keys() or source_path != item.resolve():
            if item.is_file():
                # Отримуємо розширення файлу (наприклад, '.jpg', '.txt')
                file_extension = item.suffix

                for file_type, extensions in file_extensions.items():
                    # Перевіряємо, чи розширення файлу входить до списку розширень для даного типу файлів
                    if file_extension[1:].upper() in extensions:
                        # Створюємо каталог призначення для даного типу файлу (якщо він ще не існує)
                        destination_directory = Path(destination_path) / file_type
                        destination_directory.mkdir(exist_ok=True)

                        # Переміщуємо файл у відповідний каталог
                        shutil.move(item, destination_directory / item.name)
                        break
                else:
                    # Якщо розширення файлу не відповідає жодному типу, переміщуємо його у каталог 'unknown'
                    destination_directory = Path(destination_path) / 'unknown'
                    destination_directory.mkdir(exist_ok=True)
                    shutil.move(item, destination_directory / item.name)

            elif item.is_dir():
                # Якщо це каталог, перевіряємо, чи він має вміст
                if any(item.iterdir()):
                    # Рекурсивно викликаємо функцію для сортування файлів у внутрішньому каталозі
                    sort_files_recursive(item, destination_path)
                else:
                    # Якщо каталог порожній, видаляємо його
                    item.rmdir()


def delete_empty_folders_recursive(directory):
    for item in directory.iterdir():
        if item.is_dir():
            # Якщо це каталог, рекурсивно викликаємо функцію для видалення порожніх каталогів
            delete_empty_folders_recursive(item)
            try:
                # Видаляємо каталог, якщо він порожній
                item.rmdir()
            except OSError:
                # Пропустити, якщо каталог не порожній
                continue


def main():
    while True:
        print("1. Сортувати каталог")
        print("2. Вихід")
        choice = input("Введіть значення для вибору ")
        if choice == "1":
            # Отримати шлях до вихідного каталогу від користувача
            source_path = input('Введіть повний шлях до вашого каталогу ')
            # Перевірка операційної системи
            if platform.system() == "Windows":
                if len(source_path.split(":")[0]) > 1:
                    # Отримати поточний робочий каталог
                    current_directory = Path.cwd()
                    # Створити повний шлях
                    source_path = current_directory / source_path

            # Перевірка, чи існує шлях та чи є це каталог
            source_directory = Path(source_path)
            if source_directory.exists() and source_directory.is_dir():
                print(f"Каталог '{source_path}' існує.")
                # Створити каталоги для сортування файлів
                for file_type in file_extensions.keys():
                    destination_directory = source_directory / file_type
                    destination_directory.mkdir(exist_ok=True)

                sort_files_recursive(source_path, source_path)
                delete_empty_folders_recursive(source_directory)
                print("Сортування завершено!")

            else:
                print(f"Каталог '{source_path}' не існує або це не каталог.")
        elif choice == "2":
            os.system('cls')
            break
        else:
            print('Некоректний вибір, спробуйте ще раз')
            time.sleep(2)
            os.system('cls')


if __name__ == '__main__':
    main()
