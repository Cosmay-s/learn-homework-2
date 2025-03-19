"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
from pathlib import Path


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file_path = Path('referat.txt')
    content = file_path.read_text(encoding='utf-8')
    print(f"Длина текста: {len(content)} символов")
    word_count = len(content.split())
    print(f"Количество слов: {word_count}")
    modified_content = content.replace('.', '!')
    result_path = Path('referat2.txt')
    result_path.write_text(modified_content, encoding='utf-8')


if __name__ == "__main__":
    main()
