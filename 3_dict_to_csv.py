"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
people_dict = [
    {"name": "Анна", "age": 25, "job": "инженер"},
    {"name": "Максим", "age": 30, "job": "учитель"},
    {"name": "Ольга", "age": 28, "job": "врач"},
    {"name": "Иван", "age": 35, "job": "программист"}
]

import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('people.csv', 'w', encoding='utf-8', newline='') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for people in people_dict:
            writer.writerow(people)

if __name__ == "__main__":
    main()
