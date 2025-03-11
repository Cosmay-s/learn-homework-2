"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file = 'referat.txt'
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()
        print(len(content.split()))
    with open('referat2.txt', 'w', encoding='utf-8') as result:
        result.write(content.replace('.', '!'))



if __name__ == "__main__":
    main()
