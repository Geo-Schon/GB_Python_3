"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. Верните все возможные варианты комплектации рюкзака.
"""

from random import randint


def variants(objects: list) -> dict:
    result_dict = {}
    for object in objects:
        result_dict[object] = randint(1, 5)
    return result_dict


list_things = ['палатка', 'компас', 'котелок', 'спички', 'термос', 'аптечка', 'топор', 'спальник', 'ложка', 'вилка']
items = variants(list_things)

max_weight = 10
current_weight = 0
backpack = {}

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight

print(f'В рюкзак вместительностью {max_weight} кг поместились следующие вещи:')
for item, weight in backpack.items():
    print(f' * {item} - {weight} кг')
