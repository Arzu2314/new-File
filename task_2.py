def copy_line(source_file_path, destination_file_path, line_number):
    try:
        with open(source_file_path, 'r') as source_file:
            lines = source_file.readlines()
            if 0 < line_number <= len(lines):
                line_to_copy = lines[line_number - 1]  # Строки в Python индексируются с 0
                with open(destination_file_path, 'a') as destination_file:
                    destination_file.write(line_to_copy)
                    print("Строка успешно скопирована в другой файл.")
            else:
                print("Некорректный номер строки.")
    except FileNotFoundError:
        print("Файл не найден.")

def main():
    source_file_path = input("Введите путь к исходному файлу: ")
    destination_file_path = input("Введите путь к файлу, куда нужно скопировать строку: ")
    line_number = int(input("Введите номер строки для копирования: "))

    copy_line(source_file_path, destination_file_path, line_number)

if __name__ == "__main__":
    main()