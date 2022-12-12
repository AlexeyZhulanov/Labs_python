import csv
import os
from functools import reduce


def get_count(data: 'list[list[int, str, float]]', gender) -> int:

    return reduce(
        lambda x, y: x + y,
        list(map(lambda row: 1 if(row[1] == gender) else 0, data))
    )


def get_summary_age(data: 'list[list[int, str, float]]', gender) -> float:
    return reduce(
        lambda x, y: x + y,
        list(map(lambda row: row[2] if(row[1] == gender) else 0, data))
    )


def get_average_age(data: 'list[list[int, str, float]]', gender) -> float:
    return get_summary_age(data, gender) / get_count(data, gender)


def get_count_class_persons(data: 'list[list[int, str, float]]', klas) -> int:
    return reduce(
        lambda x, y: x + y,
        list(map(lambda row: 1 if (row[0] == klas) else 0, data))
    )


def get_max_class_persons(data: 'list[list[int, str, float]]') -> int:
    mas = [get_count_class_persons(data, 1), get_count_class_persons(data, 2), get_count_class_persons(data, 3)]
    return mas.index(max(mas))+1


def filter_rows(data: 'list[list]') -> 'list[list]':
    return list(filter(lambda row: row[0] != 0, data))


def get_valid_data(filename: str) -> 'list[list[int, str, float]]':
    return transform_data(retrieve_cols(filter_rows(read_data(filename))))


def read_data(filename: str) -> 'list[list]':
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
    with open(path, 'r') as file:
        return list(csv.reader(file, delimiter=','))[1:]


def replace_cols(row: 'list[str, str, str]'
                 ) -> 'list[int, str, float]':
    return [
        int(row[0]),
        row[1],
        float(row[2])
    ]


def retrieve_cols(data: 'list[list]') -> 'list[list[str, str, str]]':
    return list(map(lambda row: [row[i] for i in (1, 3, 4)], data))


def transform_data(data: 'list[list[str, str, str]]'
                   ) -> 'list[list[int, str, float]]':
    return list(map(replace_cols, data))


data = get_valid_data('titanic.csv')
males_average_age = get_average_age(data, 'male')
females_average_age = get_average_age(data, 'female')
max_alived_class = get_max_class_persons(data)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(
        f'Средний возраст у выживших мужчин: {males_average_age:.3f}\n'
    )
    file.write(
        f'Средний возраст у выживших женщин: {females_average_age:.3f}\n'
    )
    file.write(
        f'Преобладают выжившие из класса: {max_alived_class:}\n'
    )